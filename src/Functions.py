from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings, QTimer
from PySide6.QtGui import QColor, QFont, QFontDatabase
from PySide6.QtWidgets import QSizePolicy, QSpacerItem
from analyticsPage import AnalyticsPage
from employeesPage import EmployeePage
from profile import ProfileWindow
from questionsPage import QuestionsPage
from answersPage import AnswersPage


class GuiFunctions():
    def __init__(self, MainWindow):
        self.main = MainWindow
        self.ui = MainWindow.ui

        self._init_font()
        self._init_theme()
        self._init_pages()
        self._connect_buttons()

        self.ui.mainPages.setCurrentWidget(self.ui.helloPage)

    def _init_font(self):
        """Загружает и применяет шрифт Ubuntu"""
        font_id = QFontDatabase.addApplicationFont("D:/pycharm/HiHire/fonts/fontRU/Ubuntu-Regular.ttf")
        if font_id == -1:
            print("Не удалось загрузить шрифт Ubuntu")
            ubuntu_font = QFont("Sans Serif")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)
            ubuntu_font = QFont(font_family[0], 9) if font_family else QFont("Sans Serif")

        self.main.setFont(ubuntu_font)
        QApplication.setFont(ubuntu_font)

    def _init_theme(self):
        """Инициализирует тему приложения"""
        settings = QSettings()
        current_theme = settings.value("THEME")
        self._populate_theme_list(current_theme)
        self.ui.themeList.currentTextChanged.connect(self._change_app_theme)

    def _populate_theme_list(self, current_theme):
        """Заполняет список доступных тем"""
        self.ui.themeList.clear()
        added_themes = set()

        for theme in self.ui.themes:
            if theme.name in ["LightBlue", "DarkBlue"] and theme.name not in added_themes:
                self.ui.themeList.addItem(theme.name, theme.name)
                added_themes.add(theme.name)
                if theme.defaultTheme or theme.name == current_theme:
                    self.ui.themeList.setCurrentText(theme.name)

    def _change_app_theme(self):
        """Изменяет тему приложения"""
        settings = QSettings()
        selected_theme = self.ui.themeList.currentData()
        current_theme = settings.value("THEME")

        if current_theme != selected_theme:
            settings.setValue("THEME", selected_theme)
            QAppSettings.updateAppSettings(self.main, reloadJson=True)

    def _init_pages(self):
        """Инициализирует страницы приложения"""
        self.questions_page = QuestionsPage(self.ui, self.main)
        self.answers_page = AnswersPage(self.ui, self.main)
        self.employee_page = EmployeePage(self.ui, self.main)
        self.analytics_page = AnalyticsPage(self.ui, self.main)

    def _connect_buttons(self):
        """Подключает кнопки меню и навигации"""
        # Центральное меню
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.closeLeftMenuBtn.clicked.connect(lambda: self.ui.centerMenu.collapseMenu())
        self.ui.prifileBtn.clicked.connect(self._show_profile_window)

        # Навигация
        self.ui.questionsBtn.clicked.connect(self.show_questions_page)
        self.ui.reportsBtn.clicked.connect(self.show_reports_page)
        self.ui.workersBtn.clicked.connect(self.show_employees_page)
        self.ui.analysisBtn.clicked.connect(self.show_analytics_page)
        self.ui.exitFromQuestionBtn.clicked.connect(self.questions_page.return_to_questions_page)
        self.ui.exitFromCandidateBtn.clicked.connect(self.answers_page.return_to_reports_page)
        self.ui.exitFromEmployeeBtn.clicked.connect(self.employee_page.return_to_employees_page)

    def show_questions_page(self):
        """Показывает страницу с вопросами и загружает шаблоны"""
        self.questions_page.bind_system_templates()
        self.questions_page.load_user_templates()

    def show_reports_page(self):
        """Показывает страницу с отчетами и загружает данные"""
        self.answers_page.init_reports_page(self.main.role_id, self.main.user_id)

    def show_employees_page(self):
        """Показывает страницу с сотрудниками и загружает данные"""
        self.employee_page.init_employees_page(self.main.role_id)

    def show_analytics_page(self):
        """Показывает страницу аналитики и обновляет данные"""
        self.analytics_page.init_analytic(self.main.role_id, self.main.user_id)

    def _show_profile_window(self):
        """Показывает окно профиля пользователя"""
        if hasattr(self, 'profile_window') and self.profile_window:
            self.profile_window.close()

        self.profile_window = ProfileWindow(self.main)
        self.profile_window.set_user_info(self.main.user_id, self.main.role_id)
        self.profile_window.logout_requested.connect(self.main.handle_logout)
        self.profile_window.show()