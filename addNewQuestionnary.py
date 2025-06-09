from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QTabWidget, QListWidget,
                               QLineEdit, QComboBox, QSpinBox, QPushButton, QFormLayout,
                               QGroupBox, QMessageBox, QScrollArea, QWidget, QCheckBox)
from PySide6.QtCore import Qt


class AddQuestionnaireDialog(QDialog):
    def __init__(self, db, user_id, role_id, parent=None):
        """Инициализирует диалог создания нового шаблона опроса"""
        super().__init__(parent)
        self.db = db
        self.user_id = user_id
        self.role_id = role_id
        self.setWindowTitle("Создать новый шаблон опроса")
        self.setMinimumSize(800, 600)

        self.init_ui()
        self.load_data()

    def init_ui(self):
        """Инициализирует пользовательский интерфейс диалога"""
        main_layout = QVBoxLayout()

        # Форма для основных данных шаблона
        form_layout = QFormLayout()
        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText("Введите название шаблона")
        self.description_edit = QLineEdit()
        self.description_edit.setPlaceholderText("Введите описание (необязательно)")
        self.position_combo = QComboBox()
        self.is_public_check = QCheckBox("Сделать шаблон публичным")
        self.is_public_check.setVisible(self.role_id == 1)

        form_layout.addRow("Название:", self.title_edit)
        form_layout.addRow("Описание:", self.description_edit)
        form_layout.addRow("Должность:", self.position_combo)
        form_layout.addRow("", self.is_public_check)

        # Вкладки для работы с вопросами
        self.tabs = QTabWidget()
        self.existing_questions_tab = QWidget()
        self.init_existing_questions_tab()
        self.tabs.addTab(self.existing_questions_tab, "Существующие вопросы")

        self.new_questions_tab = QWidget()
        self.init_new_questions_tab()
        self.tabs.addTab(self.new_questions_tab, "Новые вопросы")

        # Список выбранных вопросов
        self.selected_questions_group = QGroupBox("Выбранные вопросы")
        self.selected_questions_layout = QVBoxLayout()
        self.selected_questions_list = QListWidget()
        self.selected_questions_list.setSelectionMode(QListWidget.SingleSelection)
        self.selected_questions_layout.addWidget(self.selected_questions_list)

        self.remove_question_btn = QPushButton("Удалить выбранный вопрос")
        self.remove_question_btn.clicked.connect(self.remove_selected_question)
        self.selected_questions_layout.addWidget(self.remove_question_btn)
        self.selected_questions_group.setLayout(self.selected_questions_layout)

        # Кнопки сохранения/отмены
        button_layout = QHBoxLayout()
        self.save_btn = QPushButton("Сохранить шаблон")
        self.save_btn.clicked.connect(self.save_questionnaire)
        self.cancel_btn = QPushButton("Отмена")
        self.cancel_btn.clicked.connect(self.reject)

        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.cancel_btn)

        # Сборка основного layout
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.tabs)
        main_layout.addWidget(self.selected_questions_group)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def init_existing_questions_tab(self):
        """Инициализирует вкладку для выбора существующих вопросов"""
        layout = QVBoxLayout()

        filter_layout = QHBoxLayout()
        self.category_filter = QComboBox()
        self.category_filter.addItem("Все категории", 0)
        self.answer_type_filter = QComboBox()
        self.answer_type_filter.addItem("Все типы", 0)

        filter_layout.addWidget(self.category_filter)
        filter_layout.addWidget(self.answer_type_filter)

        self.existing_questions_list = QListWidget()
        self.existing_questions_list.setSelectionMode(QListWidget.MultiSelection)

        self.add_existing_btn = QPushButton("Добавить выбранные вопросы")
        self.add_existing_btn.clicked.connect(self.add_existing_questions)

        layout.addLayout(filter_layout)
        layout.addWidget(self.existing_questions_list)
        layout.addWidget(self.add_existing_btn)

        self.existing_questions_tab.setLayout(layout)

    def init_new_questions_tab(self):
        """Инициализирует вкладку для создания новых вопросов"""
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        container = QWidget()
        layout = QVBoxLayout()

        self.new_question_group = QGroupBox("Новый вопрос")
        new_question_form = QFormLayout()

        self.new_question_text = QLineEdit()
        self.new_question_text.setPlaceholderText("Введите текст вопроса")
        self.new_question_weight = QSpinBox()
        self.new_question_weight.setRange(1, 10)
        self.new_question_weight.setValue(1)
        self.new_question_category = QComboBox()
        self.new_question_answer_type = QComboBox()

        new_question_form.addRow("Текст вопроса:", self.new_question_text)
        new_question_form.addRow("Вес вопроса:", self.new_question_weight)
        new_question_form.addRow("Категория:", self.new_question_category)
        new_question_form.addRow("Тип ответа:", self.new_question_answer_type)

        self.new_question_group.setLayout(new_question_form)

        self.options_group = QGroupBox("Варианты ответов")
        self.options_layout = QVBoxLayout()
        self.add_option_btn = QPushButton("Добавить вариант")
        self.add_option_btn.clicked.connect(self.add_option_form)
        self.options_layout.addWidget(self.add_option_btn)
        self.options_group.setLayout(self.options_layout)
        self.options_group.hide()

        self.add_new_question_btn = QPushButton("Добавить вопрос в шаблон")
        self.add_new_question_btn.clicked.connect(self.add_new_question)

        layout.addWidget(self.new_question_group)
        layout.addWidget(self.options_group)
        layout.addWidget(self.add_new_question_btn)
        layout.addStretch()

        container.setLayout(layout)
        scroll.setWidget(container)

        new_tab_layout = QVBoxLayout()
        new_tab_layout.addWidget(scroll)
        self.new_questions_tab.setLayout(new_tab_layout)

        self.new_question_answer_type.currentIndexChanged.connect(self.update_options_visibility)

    def load_data(self):
        """Загружает начальные данные (должности, категории, типы ответов) из базы данных"""
        positions = self.db.get_positions()
        for position in positions:
            self.position_combo.addItem(position['name'], position['id'])

        categories = self.db.execute_query("SELECT id, name FROM Categories")
        self.category_filter.addItem("Все категории", 0)
        self.new_question_category.addItem("Выберите категорию", 0)
        for category in categories:
            self.category_filter.addItem(category['name'], category['id'])
            self.new_question_category.addItem(category['name'], category['id'])

        answer_types = self.db.get_answer_types()
        self.answer_type_filter.addItem("Все типы", 0)
        self.new_question_answer_type.addItem("Выберите тип", 0)
        for at in answer_types:
            self.answer_type_filter.addItem(at['name'], at['id'])
            self.new_question_answer_type.addItem(at['name'], at['id'])

        self.load_existing_questions()

    def load_existing_questions(self):
        """Загружает список существующих вопросов с учетом текущих фильтров"""
        self.existing_questions_list.clear()

        category_id = self.category_filter.currentData()
        answer_type_id = self.answer_type_filter.currentData()

        query = """
        SELECT q.id, q.text, c.name as category, at.name as answer_type 
        FROM Questions q 
        JOIN Categories c ON q.category_id = c.id 
        JOIN AnswerTypes at ON q.answer_type_id = at.id 
        WHERE 1=1
        """

        params = []

        if category_id:
            query += " AND q.category_id = %s"
            params.append(category_id)

        if answer_type_id:
            query += " AND q.answer_type_id = %s"
            params.append(answer_type_id)

        query += " ORDER BY q.text"

        questions = self.db.execute_query(query, params or None)

        for question in questions:
            item_text = f"{question['text']} ({question['category']}, {question['answer_type']})"
            self.existing_questions_list.addItem(item_text)
            self.existing_questions_list.item(self.existing_questions_list.count() - 1).setData(Qt.UserRole,
                                                                                                question['id'])

    def add_existing_questions(self):
        """Добавляет выбранные существующие вопросы в список выбранных вопросов"""
        selected_items = self.existing_questions_list.selectedItems()
        for item in selected_items:
            question_id = item.data(Qt.UserRole)
            if not self.is_question_added(question_id):
                self.selected_questions_list.addItem(item.text())
                self.selected_questions_list.item(self.selected_questions_list.count() - 1).setData(Qt.UserRole, {
                    'type': 'existing',
                    'id': question_id
                })

    def add_new_question(self):
        """Добавляет новый вопрос в список выбранных вопросов после валидации"""
        if not self.new_question_text.text().strip():
            QMessageBox.warning(self, "Ошибка", "Введите текст вопроса")
            return

        if self.new_question_category.currentData() == 0:
            QMessageBox.warning(self, "Ошибка", "Выберите категорию")
            return

        if self.new_question_answer_type.currentData() == 0:
            QMessageBox.warning(self, "Ошибка", "Выберите тип ответа")
            return

        answer_type_id = self.new_question_answer_type.currentData()

        options = []
        if answer_type_id in (1, 2):
            options = self.collect_options()
            if not options:
                QMessageBox.warning(self, "Ошибка", "Добавьте хотя бы один вариант ответа")
                return

        question_data = {
            'type': 'new',
            'text': self.new_question_text.text(),
            'weight': self.new_question_weight.value(),
            'category_id': self.new_question_category.currentData(),
            'answer_type_id': answer_type_id,
            'options': options
        }

        item_text = f"{question_data['text']} (новый)"
        self.selected_questions_list.addItem(item_text)
        self.selected_questions_list.item(self.selected_questions_list.count() - 1).setData(Qt.UserRole, question_data)

        self.new_question_text.clear()
        self.clear_options_form()

    def collect_options(self):
        """Собирает варианты ответов из формы"""
        options = []
        for i in range(self.options_layout.count() - 1):
            widget = self.options_layout.itemAt(i).widget()
            if isinstance(widget, QWidget):
                text_edit = widget.findChild(QLineEdit, "option_text")
                score_spin = widget.findChild(QSpinBox, "option_score")
                if text_edit and score_spin:
                    options.append({
                        'text': text_edit.text(),
                        'score': score_spin.value()
                    })
        return options

    def add_option_form(self):
        """Добавляет новую форму для варианта ответа"""
        option_widget = QWidget()
        option_layout = QHBoxLayout(option_widget)

        text_edit = QLineEdit()
        text_edit.setPlaceholderText("Текст варианта")
        text_edit.setObjectName("option_text")

        score_spin = QSpinBox()
        score_spin.setRange(0, 10)
        score_spin.setValue(1)
        score_spin.setObjectName("option_score")

        remove_btn = QPushButton("×")
        remove_btn.setFixedSize(25, 25)
        remove_btn.clicked.connect(lambda: self.remove_option_form(option_widget))

        option_layout.addWidget(text_edit)
        option_layout.addWidget(score_spin)
        option_layout.addWidget(remove_btn)

        self.options_layout.insertWidget(self.options_layout.count() - 1, option_widget)

    def remove_option_form(self, widget):
        """Удаляет форму варианта ответа"""
        for i in range(self.options_layout.count()):
            if self.options_layout.itemAt(i).widget() == widget:
                self.options_layout.removeWidget(widget)
                widget.deleteLater()
                break

    def clear_options_form(self):
        """Очищает все формы вариантов ответов"""
        while self.options_layout.count() > 1:
            item = self.options_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def update_options_visibility(self):
        """Обновляет видимость группы вариантов ответов в зависимости от выбранного типа"""
        answer_type_id = self.new_question_answer_type.currentData()
        self.options_group.setVisible(answer_type_id in (1, 2))

    def is_question_added(self, question_id):
        """Проверяет, добавлен ли вопрос в список выбранных"""
        for i in range(self.selected_questions_list.count()):
            item = self.selected_questions_list.item(i)
            data = item.data(Qt.UserRole)
            if data['type'] == 'existing' and data['id'] == question_id:
                return True
        return False

    def remove_selected_question(self):
        """Удаляет выбранный вопрос из списка выбранных"""
        selected_row = self.selected_questions_list.currentRow()
        if selected_row >= 0:
            self.selected_questions_list.takeItem(selected_row)

    def save_questionnaire(self):
        """Сохраняет шаблон опроса в базу данных"""
        if not self.title_edit.text().strip():
            QMessageBox.warning(self, "Ошибка", "Введите название шаблона")
            return

        if self.position_combo.currentIndex() < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите должность")
            return

        if self.selected_questions_list.count() == 0:
            QMessageBox.warning(self, "Ошибка", "Добавьте хотя бы один вопрос")
            return

        try:
            questionnaire_id = self.db.execute_query(
                "INSERT INTO Questionnaires (position_id, title, description, created_by, is_public) "
                "VALUES (%s, %s, %s, %s, %s)",
                (
                    self.position_combo.currentData(),
                    self.title_edit.text(),
                    self.description_edit.text(),
                    self.user_id,
                    1 if self.is_public_check.isChecked() else 0
                ),
                fetch_all=False,
                return_lastrowid=True
            )

            if not questionnaire_id:
                raise Exception("Не удалось создать шаблон")

            for i in range(self.selected_questions_list.count()):
                item = self.selected_questions_list.item(i)
                data = item.data(Qt.UserRole)

                if data['type'] == 'existing':
                    success = self.db.execute_query(
                        "INSERT INTO QuestionnaireQuestions (questionnaire_id, question_id) VALUES (%s, %s)",
                        (questionnaire_id, data['id']),
                        fetch_all=False,
                        return_lastrowid=True
                    )

                else:
                    question_id = self.db.execute_query(
                        "INSERT INTO Questions (text, weight, answer_type_id, category_id) "
                        "VALUES (%s, %s, %s, %s)",
                        (
                            data['text'],
                            data['weight'],
                            data['answer_type_id'],
                            data['category_id']
                        ),
                        fetch_all=False,
                        return_lastrowid=True
                    )

                    if not question_id:
                        print(f"Не удалось создать вопрос: {data['text']}")
                        continue

                    self.db.execute_query(
                        "INSERT INTO QuestionnaireQuestions (questionnaire_id, question_id) "
                        "VALUES (%s, %s)",
                        (questionnaire_id, question_id),
                        fetch_all=False
                    )

                    if data['answer_type_id'] in (1, 2) and data['options']:
                        for option in data['options']:
                            self.db.execute_query(
                                "INSERT INTO QuestionOptions (question_id, text, score) "
                                "VALUES (%s, %s, %s)",
                                (question_id, option['text'], option['score']),
                                fetch_all=False
                            )

            QMessageBox.information(self, "Успех", "Шаблон успешно создан!")
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить шаблон: {str(e)}")