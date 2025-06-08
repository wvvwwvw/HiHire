from datetime import datetime
from PySide6.QtWidgets import (QFrame, QVBoxLayout, QLabel, QPushButton, QWidget,
                               QHBoxLayout, QScrollArea, QMessageBox, QDialogButtonBox,
                               QLineEdit, QFormLayout, QDialog, QComboBox)
from PySide6.QtCore import Qt, Signal
from connect_to_database import Database


class EmployeePage:
    def __init__(self, ui, main_window):
        self.ui = ui
        self.main_window = main_window
        self.db = Database()
        self.current_employee_id = None
        self.current_role_id = None

        self.setup_ui_connections()

    def setup_ui_connections(self):
        """Настраивает соединения сигналов и слотов"""
        self.ui.exitFromEmployeeBtn.clicked.connect(self.return_to_employees_page)
        self.ui.esaveChangesBtn.clicked.connect(self.save_employee_changes)
        self.ui.eStatusComboBox.currentIndexChanged.connect(self.filter_employees)
        self.ui.ePositionComboBox.currentIndexChanged.connect(self.filter_employees)
        self.ui.fioLineEdit.textChanged.connect(self.filter_employees)
        self.ui.eDateComboBox.currentIndexChanged.connect(self.filter_employees)
        self.ui.createUserBtn.clicked.connect(self.show_create_user_dialog)

    def init_employees_page(self, user_role_id):
        """Инициализирует страницу сотрудников"""
        self.current_role_id = user_role_id
        self.load_filters()
        self.load_employees()

    def load_filters(self):
        """Загружает данные для фильтров"""
        self.load_statuses()
        self.load_positions()
        self.load_date_sort_options()

    def load_statuses(self):
        """Загружает статусы сотрудников"""
        statuses = self.db.execute_query("SELECT id, name FROM Statuses WHERE type = 'empl'")
        self.ui.eStatusComboBox.clear()
        self.ui.eStatusComboBox.addItem("Все статусы", None)
        for status in statuses:
            self.ui.eStatusComboBox.addItem(status['name'], status['id'])

    def load_positions(self):
        """Загружает список должностей"""
        positions = self.db.execute_query("SELECT id, name FROM Positions")
        self.ui.ePositionComboBox.clear()
        self.ui.ePositionComboBox.addItem("Все должности", None)
        for position in positions:
            self.ui.ePositionComboBox.addItem(position['name'], position['id'])

    def load_date_sort_options(self):
        """Настраивает варианты сортировки по дате"""
        self.ui.eDateComboBox.clear()
        self.ui.eDateComboBox.addItem("Новые сначала", "DESC")
        self.ui.eDateComboBox.addItem("Старые сначала", "ASC")

    def load_employees(self, filters=None):
        """Загружает список сотрудников с учетом фильтров"""
        self.clear_layout(self.ui.emloyeesVerticalLayout)
        self.ui.emloyeesVerticalLayout.setAlignment(Qt.AlignTop)

        query, params = self.build_employees_query(filters)
        employees = self.db.execute_query(query, params or None)

        if not employees:
            self.show_no_employees_message()
            return

        for employee in employees:
            self.add_employee_card(employee)

    def build_employees_query(self, filters):
        """Строит SQL запрос для получения сотрудников"""
        query = """
        SELECT e.id, e.first_name, e.last_name, e.patronimic, e.email, e.phone, 
               p.name as position_name, s.name as status_name,
               e.hire_date, e.fire_date, e.skills
        FROM Employees e
        JOIN Positions p ON e.position_id = p.id
        JOIN Statuses s ON e.status_id = s.id
        WHERE 1=1
        """
        params = []

        if filters:
            query, params = self.apply_employee_filters(query, params, filters)

        if filters and filters.get('date_sort'):
            query += " ORDER BY e.hire_date " + filters['date_sort']
        else:
            query += " ORDER BY e.hire_date DESC"

        return query, params

    def apply_employee_filters(self, query, params, filters):
        """Применяет фильтры к запросу сотрудников"""
        if filters.get('status_id'):
            query += " AND e.status_id = %s"
            params.append(filters['status_id'])

        if filters.get('position_id'):
            query += " AND e.position_id = %s"
            params.append(filters['position_id'])

        if filters.get('fio'):
            query += " AND (e.first_name LIKE %s OR e.last_name LIKE %s OR e.patronimic LIKE %s)"
            params.extend([f'%{filters["fio"]}%'] * 3)

        return query, params

    def show_no_employees_message(self):
        """Показывает сообщение об отсутствии сотрудников"""
        no_results_label = QLabel("Нет сотрудников, соответствующих фильтрам")
        no_results_label.setStyleSheet("font-size: 12pt;")
        self.ui.emloyeesVerticalLayout.addWidget(no_results_label)

    def add_employee_card(self, employee):
        """Добавляет карточку сотрудника"""
        frame = QFrame()
        frame.setMinimumSize(0, 100)
        frame.setMaximumHeight(100)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setStyleSheet(self.get_card_style())

        layout = QHBoxLayout(frame)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.add_left_card_content(layout, employee)
        self.add_center_card_content(layout, employee)

        if self.current_role_id == 1:
            self.add_right_card_content(layout, employee)

        frame.mousePressEvent = lambda event, e=employee: self.open_employee_page(e)
        self.ui.emloyeesVerticalLayout.addWidget(frame)

    def get_card_style(self):
        """Возвращает стиль для карточки сотрудника"""
        return f"""
            QFrame {{
                background-color: {self.main_window.theme.COLOR_BACKGROUND_1};
                border-radius: 10px;
                margin: 2px;
            }}
            QFrame:hover {{
                background-color: {self.main_window.theme.COLOR_BACKGROUND_3};
                border: {self.main_window.theme.COLOR_ACCENT_1};
            }}
        """

    def add_left_card_content(self, layout, employee):
        """Добавляет левую часть карточки (информация о сотруднике)"""
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(5)

        fio = f"{employee['last_name']} {employee['first_name']} {employee['patronimic'] or ''}"
        fio_label = QLabel(fio.strip())
        fio_label.setStyleSheet(self.get_label_style(12, True))
        left_layout.addWidget(fio_label)

        position_label = QLabel(employee['position_name'])
        position_label.setStyleSheet(self.get_label_style(11))
        left_layout.addWidget(position_label)

        layout.addWidget(left_widget, 70)

    def add_center_card_content(self, layout, employee):
        """Добавляет центральную часть карточки (статус и дата)"""
        center_widget = QWidget()
        center_layout = QVBoxLayout(center_widget)
        center_layout.setAlignment(Qt.AlignRight | Qt.AlignTop)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(5)

        status_label = QLabel(employee['status_name'])
        status_label.setStyleSheet(self.get_status_label_style())
        center_layout.addWidget(status_label)

        date_label = QLabel(employee['hire_date'].strftime('%d.%m.%Y'))
        date_label.setStyleSheet(self.get_label_style(10))
        date_label.setAlignment(Qt.AlignRight)
        center_layout.addWidget(date_label)

        layout.addWidget(center_widget, 30)

    def add_right_card_content(self, layout, employee):
        """Добавляет правую часть карточки (кнопка удаления)"""
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setAlignment(Qt.AlignRight | Qt.AlignTop)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(5)

        delete_btn = QPushButton("-")
        delete_btn.setFixedSize(100, 20)
        delete_btn.setStyleSheet(self.get_button_style())
        delete_btn.clicked.connect(lambda: self.delete_employee(employee))
        right_layout.addWidget(delete_btn)

        layout.addWidget(right_widget, 10)

    def get_label_style(self, size, bold=False):
        """Возвращает стиль для текстовых меток"""
        weight = "font-weight: bold;" if bold else ""
        return f"""
            {weight} font-size: {size}pt; 
            background-color: transparent; 
            color: {self.main_window.theme.COLOR_TEXT_1};
        """

    def get_status_label_style(self):
        """Возвращает стиль для метки статуса"""
        return f"""
            font-size: 11pt; 
            font-weight: bold; 
            color: {self.main_window.theme.COLOR_TEXT_1};
            background-color: {self.main_window.theme.COLOR_ACCENT_1};
            border-radius: 10px;
            padding: 2px 5px;
        """

    def get_button_style(self):
        """Возвращает стиль для кнопок"""
        return f"""
            QPushButton {{
                background-color: {self.main_window.theme.COLOR_ACCENT_1};
                color: {self.main_window.theme.COLOR_TEXT_1};
                border-radius: 10px;
                font-size: 10pt;
            }}
            QPushButton:hover {{
                background-color: {self.main_window.theme.COLOR_ACCENT_2};
            }}
        """

    def open_employee_page(self, employee):
        """Открывает страницу с подробной информацией о сотруднике"""
        self.current_employee_id = employee['id']
        self.update_employee_info(employee)
        self.setup_employee_actions(employee)

    def update_employee_info(self, employee):
        """Обновляет информацию о сотруднике на странице"""
        self.ui.employeeNameLineEdit.setText(
            f"{employee['first_name']} {employee['last_name']} {employee['patronimic'] or ''}")

        self.ui.employeePositionComboBox.clear()
        positions = self.db.execute_query("SELECT id, name FROM Positions")
        current_pos_index = 0
        for i, position in enumerate(positions):
            self.ui.employeePositionComboBox.addItem(position['name'], position['id'])
            if position['id'] == employee.get('position_id', 0):
                current_pos_index = i
        self.ui.employeePositionComboBox.setCurrentIndex(current_pos_index)

        self.ui.employeeEmailLineEdit.setText(employee['email'])
        self.ui.employeePhoneLineEdit.setText(employee['phone'])
        self.ui.dateStart.setText(employee['hire_date'].strftime('%d.%m.%Y'))
        self.ui.dateFire.setText(employee['fire_date'].strftime('%d.%m.%Y') if employee['fire_date'] else " ")

        self.update_worked_period(employee)
        self.update_skills_display(employee)
        self.update_user_info_display(employee['id'])

    def update_skills_display(self, employee):
        """Обновляет отображение навыков сотрудника"""
        if employee['skills']:
            try:
                skills_dict = eval(employee['skills']) if isinstance(employee['skills'], str) else employee['skills']
                if isinstance(skills_dict, dict):
                    formatted_skills = []
                    for category, skills in skills_dict.items():
                        if skills:
                            replaced_skills = skills.replace(', ', '\n  - ')
                            formatted_skills.append(f"{category}:\n  - {replaced_skills}")
                    self.ui.skillsTextEdit.setPlainText("\n\n".join(formatted_skills))
                else:
                    self.ui.skillsTextEdit.setPlainText(str(skills_dict))
            except:
                self.ui.skillsTextEdit.setPlainText(str(employee['skills']))
        else:
            self.ui.skillsTextEdit.setPlainText("Нет информации о навыках")

    def delete_employee(self, employee):
        """Удаляет сотрудника с подтверждением (только для админа)"""
        confirm_dialog = QMessageBox(self.main_window)
        confirm_dialog.setWindowTitle("Подтверждение удаления")
        confirm_dialog.setText(
            f"Вы уверены, что хотите удалить сотрудника {employee['last_name']} {employee['first_name']}?"
        )

        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setButtonText(QMessageBox.Yes, "Да")
        confirm_dialog.setButtonText(QMessageBox.No, "Нет")
        confirm_dialog.setDefaultButton(QMessageBox.No)
        confirm_dialog.setIcon(QMessageBox.Warning)

        confirm_dialog.setStyleSheet(f"""
            QMessageBox {{
                background-color: {self.main_window.theme.COLOR_BACKGROUND_1};
                color: {self.main_window.theme.COLOR_TEXT_1};
            }}
            QMessageBox QLabel {{
                color: {self.main_window.theme.COLOR_TEXT_1};
            }}
        """)

        if confirm_dialog.exec() == QMessageBox.Yes:
            try:

                try:
                    self.db.execute_query(
                        "DELETE FROM Users WHERE employee_id = %s",
                        (employee['id'],)
                    )
                except:
                    return

                self.db.execute_query(
                    "DELETE FROM Employees WHERE id = %s",
                    (employee['id'],)
                )

                self.load_employees()

                if self.current_employee_id == employee['id']:
                    self.return_to_employees_page()

                QMessageBox.information(
                    self.main_window,
                    "Удаление завершено",
                    "Сотрудник успешно удален.",
                    QMessageBox.Ok
                )
            except Exception as e:
                print(f"Ошибка при удалении сотрудника: {e}")
                QMessageBox.critical(
                    self.main_window,
                    "Ошибка удаления",
                    f"Произошла ошибка при удалении: {str(e)}",
                    QMessageBox.Ok
                )

    def open_employee_page(self, employee):
        """Открывает страницу сотрудника с подробной информацией"""
        self.current_employee_id = employee['id']

        self.update_user_info_display(employee['id'])

        self.ui.employeeStatus.setText(employee['status_name'])
        self.ui.employeeStatus.setStyleSheet(f"""
            font-size: 11pt; 
            font-weight: bold; 
            color: {self.main_window.theme.COLOR_TEXT_1};
            background-color: {self.main_window.theme.COLOR_ACCENT_1};
            border-radius: 10px;
            padding: 2px 5px;
        """)

        self.ui.employeeNameLineEdit.setText(
            f"{employee['first_name']} {employee['last_name']} {employee['patronimic'] or ''}")
        self.ui.employeePositionComboBox.clear()

        positions = self.db.execute_query("SELECT id, name FROM Positions")
        current_pos_index = 0
        for i, position in enumerate(positions):
            self.ui.employeePositionComboBox.addItem(position['name'], position['id'])
            if position['id'] == employee.get('position_id', 0):
                current_pos_index = i
        self.ui.employeePositionComboBox.setCurrentIndex(current_pos_index)

        self.ui.employeeEmailLineEdit.setText(employee['email'])
        self.ui.employeePhoneLineEdit.setText(employee['phone'])
        self.ui.dateStart.setText(employee['hire_date'].strftime('%d.%m.%Y'))

        if employee['fire_date']:
            self.ui.dateFire.setText(employee['fire_date'].strftime('%d.%m.%Y'))
        else:
            self.ui.dateFire.hide()
            self.ui.label_26.hide()

        self.update_worked_period(employee)

        if employee['skills']:
            self.ui.skillsTextEdit.setPlainText(", ".join(employee['skills']))
        else:
            self.ui.skillsTextEdit.setPlainText("")

        if employee['skills']:
            try:
                skills_dict = eval(employee['skills']) if isinstance(employee['skills'], str) else employee['skills']

                if isinstance(skills_dict, dict):
                    formatted_skills = []
                    for category, skills in skills_dict.items():
                        if skills:
                            replaced_skills = skills.replace(', ', '\n  - ')
                            formatted_skills.append(f"{category}:\n  - {replaced_skills}")

                    self.ui.skillsTextEdit.setPlainText("\n\n".join(formatted_skills))
                else:
                    self.ui.skillsTextEdit.setPlainText(str(skills_dict))
            except:
                self.ui.skillsTextEdit.setPlainText(str(employee['skills']))
        else:
            self.ui.skillsTextEdit.setPlainText("Нет информации о навыках")

        self.setup_buttons_based_on_status(employee['status_name'])

        self.connect_buttons_handlers(employee)

        self.ui.mainPages.setCurrentWidget(self.ui.employeePage)

    def update_worked_period(self, employee):
        """Рассчитывает и отображает срок работы сотрудника"""
        from datetime import datetime

        hire_date = employee['hire_date']
        fire_date = employee.get('fire_date')
        today = datetime.now().date()

        if fire_date:
            end_date = fire_date
        else:
            end_date = today

        delta = end_date - hire_date
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30

        period_parts = []
        if years > 0:
            period_parts.append(f"{years} г.")
        if months > 0:
            period_parts.append(f"{months} мес.")
        if days > 0 or not period_parts:
            period_parts.append(f"{days} дн.")

        period_text = " ".join(period_parts)
        self.ui.workedInCompany.setText(period_text)

    def setup_buttons_based_on_status(self, current_status):
        """Настраивает видимость кнопок в зависимости от статуса сотрудника"""
        self.ui.firedBtn.hide()
        self.ui.vacationBtn.hide()
        self.ui.workingBtn.hide()

        if current_status == "Работает":
            self.ui.firedBtn.show()
            self.ui.vacationBtn.show()
        elif current_status == "В отпуске":
            self.ui.firedBtn.show()
            self.ui.workingBtn.show()
        elif current_status == "На испытательном сроке":
            self.ui.firedBtn.show()
            self.ui.workingBtn.show()

    def connect_buttons_handlers(self, employee):
        """Подключает обработчики для кнопок действий с сотрудником"""
        try:
            self.ui.firedBtn.clicked.disconnect()
            self.ui.vacationBtn.clicked.disconnect()
            self.ui.workingBtn.clicked.disconnect()
        except:
            pass

        self.ui.firedBtn.clicked.connect(lambda: self.change_employee_status(5))
        self.ui.vacationBtn.clicked.connect(lambda: self.change_employee_status(6))
        self.ui.workingBtn.clicked.connect(lambda: self.change_employee_status(1))

    def save_employee_changes(self):
        """Сохраняет изменения данных сотрудника"""
        if not self.current_employee_id:
            return

        try:
            fio_parts = self.ui.employeeNameLineEdit.text().split()
            first_name = fio_parts[0] if len(fio_parts) > 0 else ""
            last_name = fio_parts[1] if len(fio_parts) > 1 else ""
            patronimic = fio_parts[2] if len(fio_parts) > 2 else ""

            position_id = self.ui.employeePositionComboBox.currentData()
            email = self.ui.employeeEmailLineEdit.text()
            phone = self.ui.employeePhoneLineEdit.text()
            skills_text = self.ui.skillsTextEdit.toPlainText()
            try:
                skills_dict = {}
                current_category = None
                for line in skills_text.split('\n'):
                    if line.endswith(':'):
                        current_category = line[:-1]
                        skills_dict[current_category] = ""
                    elif line.startswith('  - ') and current_category:
                        skills_dict[current_category] += line[4:] + ", "

                for category in skills_dict:
                    if skills_dict[category].endswith(', '):
                        skills_dict[category] = skills_dict[category][:-2]

                skills = str(skills_dict)
            except:
                skills = skills_text

            self.db.execute_query(
                "UPDATE Employees SET first_name = %s, last_name = %s, patronimic = %s, "
                "position_id = %s, email = %s, phone = %s, skills = %s WHERE id = %s",
                (first_name, last_name, patronimic, position_id, email, phone, skills, self.current_employee_id),
                fetch_all=False
            )

            self.main_window.show_success_message("Данные сотрудника успешно обновлены")

            self.load_employees()

        except Exception as e:
            print(f"Ошибка при сохранении данных сотрудника: {e}")
            self.main_window.show_error_message("Ошибка при сохранении данных")

    def change_employee_status(self, status_id):
        """Изменяет статус сотрудника"""
        if not self.current_employee_id:
            return

        try:
            status = self.db.execute_query(
                "SELECT name FROM Statuses WHERE id = %s",
                (status_id,),
                fetch_all=False
            )

            if status:
                update_query = "UPDATE Employees SET status_id = %s"
                params = [status_id]

                if status_id == 5:  # Уволен
                    update_query += ", fire_date = CURRENT_DATE"
                elif status_id in (1, 6):
                    update_query += ", fire_date = NULL"

                update_query += " WHERE id = %s"
                params.append(self.current_employee_id)

                self.db.execute_query(update_query, params, fetch_all=False)

                employee = self.db.execute_query(
                    "SELECT * FROM Employees WHERE id = %s",
                    (self.current_employee_id,),
                    fetch_all=False
                )

                if employee:
                    self.ui.employeeStatus.setText(status['name'])
                    self.update_worked_period(employee)

                    if status_id == 5:
                        self.ui.dateFire.setText(datetime.now().strftime('%d.%m.%Y'))
                    else:
                        self.ui.label_26.hide()
                        self.ui.dateFire.hide()

                    self.setup_buttons_based_on_status(status['name'])

                self.main_window.show_success_message(f"Статус сотрудника изменен на '{status['name']}'")

                self.load_employees()

        except Exception as e:
            print(f"Ошибка при изменении статуса сотрудника: {e}")
            self.main_window.show_error_message("Ошибка при изменении статуса")

    def filter_employees(self):
        """Применяет фильтры к списку сотрудников"""
        filters = {
            'status_id': self.ui.eStatusComboBox.currentData(),
            'position_id': self.ui.ePositionComboBox.currentData(),
            'fio': self.ui.fioLineEdit.text().strip(),
            'date_sort': self.ui.eDateComboBox.currentData()
        }

        self.load_employees(filters)

    def return_to_employees_page(self):
        """Возвращает на страницу списка сотрудников"""
        self.ui.mainPages.setCurrentWidget(self.ui.employeesPage)

    def clear_layout(self, layout):
        """Очищает layout от всех виджетов"""
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_layout(item.layout())

    def show_create_user_dialog(self):
        """Показывает диалог создания пользователя"""
        if not self.current_employee_id:
            return

        dialog = QMessageBox(self.main_window)
        dialog.setWindowTitle("Создание пользователя")
        dialog.setText("Введите данные для создания пользователя")

        login_edit = QLineEdit()
        password_edit = QLineEdit()
        email_password_edit = QLineEdit()
        role_combo = QComboBox()

        password_edit.setEchoMode(QLineEdit.Password)
        email_password_edit.setEchoMode(QLineEdit.Password)

        layout = QFormLayout()
        layout.addRow("Логин:", login_edit)
        layout.addRow("Пароль:", password_edit)
        layout.addRow("Пароль для почты:", email_password_edit)
        layout.addRow("Роль:", role_combo)

        dialog.setLayout(layout)

        dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        dialog.setButtonText(QMessageBox.Ok, "Создать")
        dialog.setButtonText(QMessageBox.Cancel, "Отмена")
        dialog.setDefaultButton(QMessageBox.Ok)
        dialog.setIcon(QMessageBox.Question)

        dialog.setStyleSheet(f"""
            QMessageBox {{
                background-color: {self.main_window.theme.COLOR_BACKGROUND_1};
                color: {self.main_window.theme.COLOR_TEXT_1};
            }}
            QMessageBox QLabel {{
                color: {self.main_window.theme.COLOR_TEXT_1};
            }}
        """)

        if dialog.exec() == QMessageBox.Ok:
            self.create_user_for_employee(
                self.current_employee_id,
                login_edit.text(),
                password_edit.text(),
                email_password_edit.text(),
                role_combo.currentData()
            )

    def create_user_for_employee(self, employee_id, login, password, email_password, role_id):
        """Создает пользователя для сотрудника"""
        if not login or not password:
            self.main_window.show_error_message("Логин и пароль обязательны")
            return

        try:
            cursor = self.db.connection.cursor()

            cursor.callproc('CreateUserForEmployee',
                            (employee_id, login, password, role_id, email_password))

            for result in cursor.stored_results():
                user_id = result.fetchone()
                if user_id:
                    self.db.connection.commit()
                    self.main_window.show_success_message("Пользователь успешно создан")
                    self.update_user_info_display(employee_id)
                    return

            self.db.connection.rollback()
            self.main_window.show_error_message("Ошибка при создании пользователя")
        except Exception as e:
            error_msg = str(e)
            if "У этого сотрудника уже есть пользователь" in error_msg:
                self.main_window.show_error_message("У этого сотрудника уже есть пользователь")
            elif "Сотрудник не найден или неактивен" in error_msg:
                self.main_window.show_error_message("Сотрудник не найден или неактивен")
            elif "Такой логин уже существует" in error_msg:
                self.main_window.show_error_message("Такой логин уже существует")
            elif "Логин и пароль не могут быть пустыми" in error_msg:
                self.main_window.show_error_message("Логин и пароль не могут быть пустыми")
            else:
                print(f"Ошибка при создании пользователя: {e}")
                self.main_window.show_error_message("Ошибка при создании пользователя")
        finally:
            if cursor:
                cursor.close()

    def update_user_info_display(self, employee_id):
        """Обновляет отображение информации о пользователе сотрудника"""
        user_info = self.db.execute_query(
            "SELECT r.name as role_name FROM Users u "
            "JOIN Roles r ON u.role_id = r.id "
            "WHERE u.employee_id = %s",
            (employee_id,),
            fetch_all=False
        )

        if user_info:
            self.ui.is_userLabel.setText(user_info['role_name'])
            self.ui.createUserBtn.setVisible(False)
        else:
            self.ui.is_userLabel.setText("")
            self.ui.createUserBtn.setVisible(self.current_role_id == 1)