import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from authorization import AuthWindow
from src.ui_interface import *
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomQToolTip import QCustomQToolTipFilter
from src.Functions import GuiFunctions


class HiHire(QMainWindow):
    def __init__(self, parent=None):
        """Инициализирует главное окно приложения"""
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/style.json"})
        QAppSettings.updateAppSettings(self)

        self.user_id = None
        self.role_id = None
        self.app_functions = GuiFunctions(self)

    def set_user_info(self, user_id, role_id):
        """Устанавливает информацию о пользователе"""
        self.user_id = user_id
        self.role_id = role_id
        if hasattr(self.app_functions, 'questions_page'):
            self.app_functions.questions_page.set_user_info(user_id, role_id)
        if hasattr(self.app_functions, 'answers_page'):
            self.app_functions.answers_page.init_reports_page(role_id, user_id)
        if hasattr(self.app_functions, 'analytics_page'):
            self.app_functions.analytics_page.init_analytic(role_id, user_id)
        if hasattr(self.app_functions, 'employees_page'):
            self.app_functions.employees_page.init_employees_page(role_id)

    def show_message(self, text, title, icon=QMessageBox.Information):
        """Универсальный метод для показа сообщений"""
        msg = QMessageBox(self)
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec()

    def show_success_message(self, text):
        """Показывает сообщение об успехе"""
        self.show_message(text, "Успех", QMessageBox.Information)

    def show_error_message(self, text):
        """Показывает сообщение об ошибке"""
        self.show_message(text, "Ошибка", QMessageBox.Critical)

    def handle_logout(self):
        """Обрабатывает выход из системы"""
        self.ui.mainPages.setCurrentWidget(self.ui.helloPage)
        auth_window = AuthWindow()
        auth_window.authorized.connect(self.on_successful_auth)
        self.close()
        auth_window.show()

    def on_successful_auth(self, user_id, role_id):
        """Обрабатывает успешную авторизацию"""
        self.set_user_info(user_id, role_id)
        self.show()

    def closeEvent(self, event):
        """Обрабатывает закрытие главного окна"""
        if hasattr(self.app_functions, 'profile_window'):
            self.app_functions.profile_window.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_tooltip_filter = QCustomQToolTipFilter(tailPosition="auto")
    app.installEventFilter(app_tooltip_filter)

    auth_window = AuthWindow()
    main_window = None


    def on_successful_auth(user_id, role_id):
        """Обрабатывает успешную авторизацию"""
        main_window = HiHire()
        main_window.set_user_info(user_id, role_id)
        main_window.show()
        auth_window.destroyed.connect(lambda: app.quit() if not main_window.isVisible() else None)


    auth_window.authorized.connect(on_successful_auth)
    auth_window.destroyed.connect(lambda: app.quit())
    auth_window.show()

    sys.exit(app.exec())