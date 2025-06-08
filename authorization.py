from PySide6.QtGui import QFontDatabase, QFont, QIcon
from PySide6.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QVBoxLayout, QDialog, QApplication
from PySide6.QtCore import Signal

from connect_to_database import Database
from src.ui_auth import Ui_AuthWindow
from Custom_Widgets import loadJsonStyle

from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.Widgets import *


class AuthWindow(QMainWindow):
    authorized = Signal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AuthWindow()
        self.ui.setupUi(self)
        self.db = Database()

        self.loadUbuntuFont()

        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/auth_style.json"})
        QAppSettings.updateAppSettings(self)

        self.ui.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.ui.loginBtn.clicked.connect(self.handle_login)
        self.ui.seeBtn.clicked.connect(self.show_password)
        self.ui.passwordRecoverLbl.mousePressEvent = self.handle_password_recover

        self.recovery_dialog = None
        self.init_password_recovery_dialog()

    def init_password_recovery_dialog(self):
        """Инициализация диалога восстановления пароля"""
        self.recovery_dialog = QDialog(self)
        self.recovery_dialog.setWindowTitle("Восстановление пароля")
        self.recovery_dialog.setFixedSize(400, 250)

        layout = QVBoxLayout()

        # Поля формы
        self.recovery_login_label = QLabel("Логин:")
        self.recovery_login_edit = QLineEdit()

        self.recovery_email_label = QLabel("Email сотрудника:")
        self.recovery_email_edit = QLineEdit()

        self.recovery_new_pass_label = QLabel("Новый пароль:")
        self.recovery_new_pass_edit = QLineEdit()
        self.recovery_new_pass_edit.setEchoMode(QLineEdit.Password)

        self.recovery_confirm_pass_label = QLabel("Подтвердите пароль:")
        self.recovery_confirm_pass_edit = QLineEdit()
        self.recovery_confirm_pass_edit.setEchoMode(QLineEdit.Password)

        self.recovery_submit_btn = QPushButton("Сбросить пароль")
        self.recovery_submit_btn.clicked.connect(self.handle_password_reset)

        # Добавление элементов в layout
        layout.addWidget(self.recovery_login_label)
        layout.addWidget(self.recovery_login_edit)
        layout.addWidget(self.recovery_email_label)
        layout.addWidget(self.recovery_email_edit)
        layout.addWidget(self.recovery_new_pass_label)
        layout.addWidget(self.recovery_new_pass_edit)
        layout.addWidget(self.recovery_confirm_pass_label)
        layout.addWidget(self.recovery_confirm_pass_edit)
        layout.addWidget(self.recovery_submit_btn)

        self.recovery_dialog.setLayout(layout)

    def handle_password_recover(self, event):
        """Обработчик клика по ссылке восстановления пароля"""
        self.recovery_login_edit.clear()
        self.recovery_email_edit.clear()
        self.recovery_new_pass_edit.clear()
        self.recovery_confirm_pass_edit.clear()
        self.recovery_dialog.exec()

    def handle_password_reset(self):
        """Обработчик сброса пароля"""
        login = self.recovery_login_edit.text()
        email = self.recovery_email_edit.text()
        new_password = self.recovery_new_pass_edit.text()
        confirm_password = self.recovery_confirm_pass_edit.text()

        if not all([login, email, new_password, confirm_password]):
            QMessageBox.warning(self.recovery_dialog, "Ошибка", "Все поля должны быть заполнены!")
            return

        if new_password != confirm_password:
            QMessageBox.warning(self.recovery_dialog, "Ошибка", "Пароли не совпадают!")
            return

        try:
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.callproc('ResetPassword', (login, email, new_password))

            for result in cursor.stored_results():
                reset_result = result.fetchone()
                if reset_result and reset_result['success'] == 1:
                    QMessageBox.information(self.recovery_dialog, "Успех", reset_result['message'])
                    self.recovery_dialog.accept()
                else:
                    QMessageBox.critical(self.recovery_dialog, "Ошибка",
                                         reset_result['message'] if reset_result else "Неизвестная ошибка")

            cursor.close()
        except Exception as err:
            QMessageBox.critical(self.recovery_dialog, "Ошибка", f"Ошибка при сбросе пароля: {err}")
            if 'cursor' in locals() and cursor:
                cursor.close()

    def handle_login(self):
        """Обработчик входа в систему"""
        login = self.ui.loginLineEdit.text()
        password = self.ui.passwordLineEdit.text()

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля!")
            return

        result = self.check_credentials(login, password)
        if result:
            user_id, role_id = result
            self.authorized.emit(user_id, role_id)
            self.close()
        else:
            QMessageBox.critical(self, "Ошибка", "Неверный логин или пароль")

    def check_credentials(self, login: str, password: str):
        """Проверка учетных данных с более строгой проверкой"""
        try:
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.callproc('AuthenticateUser', (login, password))

            results = []
            for result in cursor.stored_results():
                results.append(result.fetchone())

            cursor.close()

            if results and len(results) > 0:
                auth_result = results[0]
                if auth_result and auth_result.get('id') is not None and auth_result.get('role_id') is not None:
                    return auth_result['id'], auth_result['role_id']

            return None

        except Exception as err:
            print(f"Ошибка аутентификации: {err}")
            if 'cursor' in locals() and cursor:
                cursor.close()
            return None

    def loadUbuntuFont(self):
        """Загружаем и применяем шрифт для текста"""
        font_id = QFontDatabase.addApplicationFont("D:/pycharm/HiHire/fonts/fontRU/Ubuntu-Regular.ttf")
        if font_id == -1:
            print("Failed to load Ubuntu font")
            return

        font_family = QFontDatabase.applicationFontFamilies(font_id)
        if font_family:
            ubuntu_font = QFont(font_family[0], 9)
        else:
            ubuntu_font = QFont("Sans Serif")

        self.setFont(ubuntu_font)
        QApplication.setFont(ubuntu_font)


    def show_password(self):
        """Управляет видимостью пароля"""
        if self.ui.passwordLineEdit.echoMode() == QLineEdit.Password:
            self.ui.passwordLineEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.passwordLineEdit.setEchoMode(QLineEdit.Password)

    def closeEvent(self, event):
        self.db.disconnect()
        super().closeEvent(event)
