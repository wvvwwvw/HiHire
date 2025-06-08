from Custom_Widgets.Widgets import *
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog

from connect_to_database import Database
from src.ui_profile import Ui_ProfileWindow


class ProfileWindow(QMainWindow):
    logout_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ProfileWindow()
        self.ui.setupUi(self)
        self.main_window = parent
        self.user_id = None
        self.role_id = None
        self.original_data = {}
        self.db = Database()

        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/profile_style.json"})
        QAppSettings.updateAppSettings(self)

        self.ui.exitBtn.clicked.connect(self.logout)
        self.ui.saveBtn.clicked.connect(self.save_changes)
        self.ui.profilePic.mousePressEvent = self.change_profile_picture

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def set_user_info(self, user_id: int, role_id: int):
        """Установка информации о пользователе и загрузка данных"""
        self.user_id = user_id
        self.role_id = role_id
        self.load_user_data()
        self.load_organizations()

    def load_user_data(self):
        """Загрузка данных пользователя из БД"""
        query = """
            SELECT u.*, e.first_name, e.last_name, e.patronimic, e.email, e.phone, 
                   e.organization_id, o.name as organization_name, p.name as position_name
            FROM Users u
            JOIN Employees e ON u.employee_id = e.id
            JOIN Organizations o ON e.organization_id = o.id
            JOIN Positions p ON e.position_id = p.id
            WHERE u.id = %s
        """
        user_data = self.db.execute_query(query, (self.user_id,), fetch_all=False)

        if user_data:
            self.original_data = {
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'patronimic': user_data['patronimic'],
                'email': user_data['email'],
                'phone': user_data['phone'],
                'organization_id': user_data['organization_id']
            }

            self.ui.firstnameLineEdit.setText(user_data['first_name'])
            self.ui.lastnameLineEdit.setText(user_data['last_name'])
            self.ui.patronimicLineEdit.setText(user_data['patronimic'] or "")
            self.ui.phoneLineEdit.setText(user_data['phone'])
            self.ui.emailLineEdit.setText(user_data['email'])

            self.ui.fioLabel.setText(f"{user_data['first_name']} {user_data['last_name']}")
            self.ui.roleLabel.setText(user_data['position_name'])
            self.ui.organizationLabel.setText(user_data['organization_name'])

            if user_data.get('avatar'):
                pixmap = QPixmap()
                pixmap.loadFromData(user_data['avatar'])
                self.ui.profilePic.setPixmap(pixmap.scaled(140, 140, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def load_organizations(self):
        """Загрузка списка организаций в комбобокс"""
        organizations = self.db.execute_query("SELECT id, name FROM Organizations WHERE status_id = 1")

        self.ui.organizationComboBox.clear()
        for org in organizations:
            self.ui.organizationComboBox.addItem(org['name'], org['id'])

        if 'organization_id' in self.original_data:
            index = self.ui.organizationComboBox.findData(self.original_data['organization_id'])
            if index >= 0:
                self.ui.organizationComboBox.setCurrentIndex(index)

    def logout(self):
        """Выход из профиля и возврат на страницу авторизации"""
        self.logout_requested.emit()
        self.close()

    def save_changes(self):
        """Сохранение изменений данных пользователя"""
        new_data = {
            'first_name': self.ui.firstnameLineEdit.text(),
            'last_name': self.ui.lastnameLineEdit.text(),
            'patronimic': self.ui.patronimicLineEdit.text(),
            'email': self.ui.emailLineEdit.text(),
            'phone': self.ui.phoneLineEdit.text(),
            'organization_id': self.ui.organizationComboBox.currentData()
        }

        if new_data == self.original_data:
            self.main_window.show_success_message("Нет изменений для сохранения")
            return

        query = """
            UPDATE Employees e
            JOIN Users u ON e.id = u.employee_id
            SET e.first_name = %s, e.last_name = %s, e.patronimic = %s, 
                e.email = %s, e.phone = %s, e.organization_id = %s
            WHERE u.id = %s
        """
        result = self.db.execute_query(query, (
            new_data['first_name'],
            new_data['last_name'],
            new_data['patronimic'],
            new_data['email'],
            new_data['phone'],
            new_data['organization_id'],
            self.user_id
        ), fetch_all=False)

        if result is not None:
            self.main_window.show_success_message("Данные успешно сохранены")
            self.original_data = new_data
        else:
            print(result)

    def change_profile_picture(self, event):
        """Изменение фотографии профиля"""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self, "Выберите изображение", "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if file_path:
            try:
                pixmap = QPixmap(file_path)
                self.ui.profilePic.setPixmap(pixmap.scaled(140, 140, Qt.KeepAspectRatio, Qt.SmoothTransformation))

                with open(file_path, 'rb') as file:
                    image_data = file.read()

                query = "UPDATE Users SET avatar = %s WHERE id = %s"
                self.db.execute_query(query, (image_data, self.user_id), fetch_all=False)

                self.main_window.show_success_message("Фотография профиля обновлена")

            except Exception as err:
                self.main_window.show_error_message(f"Ошибка загрузки изображения: {err}")


    def closeEvent(self, event):
        """Закрытие соединения с БД при закрытии окна"""
        self.db.disconnect()
        event.accept()