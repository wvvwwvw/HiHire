from PySide6.QtWidgets import (QFrame, QVBoxLayout, QLabel, QPushButton, QTextEdit,
                               QWidget, QCheckBox, QSlider, QRadioButton, QButtonGroup,
                               QHBoxLayout, QMessageBox, QDialog, QScrollArea, QGridLayout)
from PySide6.QtCore import Qt, QSize
from addNewQuestionnary import AddQuestionnaireDialog
from connect_to_database import Database


class QuestionsPage:
    def __init__(self, ui, main_window):
        self.ui = ui
        self.main_window = main_window
        self.db = Database()
        self.user_id = None
        self.role_id = None

        self.setup_ui_connections()
        self.bind_system_templates()

    def setup_ui_connections(self):
        """Настраивает соединения сигналов и слотов"""
        self.ui.exitFromQuestionBtn.clicked.connect(self.return_to_questions_page)
        self.ui.addQuestionaryBtn.clicked.connect(self.show_add_questionary_dialog)
        self.ui.saveQuestionsBtn.clicked.connect(self.save_questionnaire_results)

    def set_user_info(self, user_id, role_id):
        """Устанавливает информацию о пользователе"""
        self.user_id = user_id
        self.role_id = role_id
        self.load_user_templates()

    def bind_system_templates(self):
        """Привязывает системные шаблоны анкет"""
        self.clear_layout(self.ui.systemTemplates.layout())

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        container = QWidget()
        scroll_area.setWidget(container)
        h_layout = QHBoxLayout(container)
        h_layout.setSpacing(15)
        h_layout.setContentsMargins(5, 5, 5, 5)

        system_templates = self.db.get_questionnaires(is_public=True, limit=6)
        for template in system_templates:
            self.add_template_card(template, h_layout, is_system=True)

        self.ui.systemTemplates.layout().addWidget(scroll_area)

    def load_user_templates(self):
        """Загружает пользовательские шаблоны анкет"""
        self.clear_layout(self.ui.usersTemplates.layout())

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        container = QWidget()
        scroll_area.setWidget(container)
        grid_layout = QGridLayout(container)
        grid_layout.setSpacing(10)
        grid_layout.setContentsMargins(5, 5, 5, 5)

        user_id = self.user_id if self.role_id != 1 else None
        user_templates = self.db.get_questionnaires(is_public=False, user_id=user_id)

        for i, template in enumerate(user_templates):
            row = i // 3
            col = i % 3
            frame = self.add_template_card(template, grid_layout)
            if frame:
                grid_layout.addWidget(frame, row, col)

        self.ui.usersTemplates.layout().addWidget(scroll_area)

    def add_template_card(self, template, layout, is_system=False):
        """Создает карточку шаблона анкеты"""
        frame = QFrame()
        frame.setMinimumSize(0, 150)
        frame.setMaximumSize(250, 150)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setStyleSheet(self.get_template_card_style())

        main_layout = QVBoxLayout(frame)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(5)

        self.add_template_header(main_layout, template, is_system)
        self.add_template_footer(main_layout, template)

        frame.mousePressEvent = lambda event, t=template: self.open_questionnaire(t)
        layout.addWidget(frame)

        return frame

    def get_template_card_style(self):
        """Возвращает стиль для карточки шаблона"""
        return f"""
            QFrame {{
                background-color: {self.main_window.theme.COLOR_BACKGROUND_1};
                border-radius: 10px;
                border: none;
                padding: 10px;
                margin: 5px;
            }}
            QFrame:hover {{
                background-color: {self.main_window.theme.COLOR_BACKGROUND_3};
            }}
        """

    def add_template_header(self, layout, template, is_system):
        """Добавляет заголовок карточки шаблона"""
        top_row = QWidget()
        top_row_layout = QHBoxLayout(top_row)
        top_row_layout.setContentsMargins(0, 0, 0, 0)
        top_row_layout.setSpacing(5)

        title_label = QLabel(template['title'])
        title_label.setWordWrap(True)
        title_label.setMinimumHeight(90)
        title_label.setStyleSheet("font-size:12pt; background: transparent;")
        top_row_layout.addWidget(title_label, 1)

        if self.role_id == 1:
            delete_btn = self.create_delete_button(template)
            top_row_layout.addWidget(delete_btn, 0, Qt.AlignRight)

        layout.addWidget(top_row)

    def create_delete_button(self, template):
        """Создает кнопку удаления шаблона"""
        delete_btn = QPushButton("-")
        delete_btn.setFixedSize(80, 25)
        delete_btn.setStyleSheet(self.get_delete_button_style())
        delete_btn.clicked.connect(lambda: self.delete_template(template))
        return delete_btn

    def get_delete_button_style(self):
        """Возвращает стиль для кнопки удаления"""
        return f"""
            QPushButton {{
                background-color: {self.main_window.theme.COLOR_ACCENT_1};
                color: {self.main_window.theme.COLOR_TEXT_1};
                border-radius: 5px;
                font-size: 9pt;
                padding: 2px;
            }}
            QPushButton:hover {{
                background-color: {self.main_window.theme.COLOR_ACCENT_2};
            }}
        """

    def add_template_footer(self, layout, template):
        """Добавляет подвал карточки шаблона"""
        max_score = self.db.get_max_score_for_questionnaire(template['id'])
        score_label = QLabel(f"Макс. баллов: {max_score}")
        score_label.setStyleSheet("font-size:9pt; background: transparent;")
        layout.addWidget(score_label, 0, Qt.AlignLeft | Qt.AlignBottom)

    def delete_template(self, template):
        """Удаляет шаблон анкеты"""
        confirm_dialog = self.create_confirmation_dialog(
            "Подтверждение удаления",
            f"Вы уверены, что хотите удалить шаблон '{template['title']}'?"
        )

        if confirm_dialog.exec() == QMessageBox.Yes:
            try:
                interviews = self.db.execute_query(
                    "SELECT COUNT(*) as cnt FROM interviews WHERE questionnaire_id = %s",
                    (template['id'],),
                    fetch_all=True
                )

                if interviews and interviews[0]['cnt'] > 0:
                    self.main_window.show_error_message(
                        "Нельзя удалить шаблон, так как существуют связанные интервью. "
                        "Сначала удалите все связанные интервью."
                    )
                    return

                self.db.execute_query(
                    "DELETE FROM QuestionnaireQuestions WHERE questionnaire_id = %s",
                    (template['id'],),
                    fetch_all=False
                )

                self.db.execute_query(
                    "DELETE FROM Questionnaires WHERE id = %s",
                    (template['id'],),
                    fetch_all=False
                )
                self.main_window.show_success_message("Шаблон успешно удален!")
                self.load_user_templates()
            except Exception as err:
                self.main_window.show_error_message(f"Не удалось удалить шаблон: {str(err)}")

    def create_confirmation_dialog(self, title, message):
        """Создает диалог подтверждения"""
        dialog = QMessageBox(self.main_window)
        dialog.setWindowTitle(title)
        dialog.setText(message)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setButtonText(QMessageBox.Yes, "Да")
        dialog.setButtonText(QMessageBox.No, "Нет")
        dialog.setDefaultButton(QMessageBox.No)
        dialog.setIcon(QMessageBox.Warning)
        dialog.setStyleSheet(self.get_dialog_style())
        return dialog

    def get_dialog_style(self):
        """Возвращает стиль для диалоговых окон"""
        return f"""
            QMessageBox {{
                background-color: {self.main_window.theme.COLOR_BACKGROUND_1};
                color: {self.main_window.theme.COLOR_TEXT_1};
            }}
            QMessageBox QLabel {{
                color: {self.main_window.theme.COLOR_TEXT_1};
            }}
        """

    def open_questionnaire(self, questionnaire):
        """Открывает анкету для заполнения"""
        self.ui.questionnaryNameLabel.setText(questionnaire['title'])
        self.ui.questionnaryNameLabel.setStyleSheet("font-size:15pt;")
        self.load_questions(questionnaire['id'])
        self.ui.mainPages.setCurrentWidget(self.ui.questionnaryPage)

    def load_questions(self, questionnaire_id):
        """Загружает вопросы анкеты"""
        self.clear_layout(self.ui.questionsBlock.layout())
        questions = self.db.get_questions_for_questionnaire(questionnaire_id)

        for question in questions:
            self.add_question_widget(question)

    def add_question_widget(self, question):
        """Добавляет виджет вопроса"""
        question_widget = QWidget()
        question_widget.setObjectName(f"question_{question['id']}")
        layout = QVBoxLayout(question_widget)

        self.add_question_text(layout, question)
        self.add_answer_controls(layout, question)

        self.ui.questionsBlock.layout().addWidget(question_widget)

    def add_question_text(self, layout, question):
        """Добавляет текст вопроса"""
        question_label = QLabel(question['text'])
        question_label.setWordWrap(True)
        question_label.setStyleSheet("font-size:12pt;")
        layout.addWidget(question_label)

    def add_answer_controls(self, layout, question):
        """Добавляет элементы управления для ответа"""
        answer_type = question['answer_type_id']

        if answer_type == 1:  # Множественный выбор
            self.add_checkbox_options(layout, question)
        elif answer_type == 2:  # Одиночный выбор
            self.add_radio_options(layout, question)
        elif answer_type in (3, 4):  # Шкала
            self.add_slider(layout, 1, 5 if answer_type == 3 else 10)
        elif answer_type == 5:  # Да/Нет
            self.add_yes_no_radio(layout)
        else:  # Свободный ответ
            self.add_text_edit(layout)

    def add_checkbox_options(self, layout, question):
        """Добавляет варианты ответа с чекбоксами"""
        options = self.db.get_options_for_question(question['id'])
        for option in options:
            checkbox = QCheckBox(option['text'])
            checkbox.setObjectName(f"option_{option['id']}")
            layout.addWidget(checkbox)

    def add_radio_options(self, layout, question):
        """Добавляет варианты ответа с радиокнопками"""
        button_group = QButtonGroup(layout.parentWidget())
        options = self.db.get_options_for_question(question['id'])
        for i, option in enumerate(options):
            radio = QRadioButton(option['text'])
            button_group.addButton(radio, option['id'])
            layout.addWidget(radio)

    def add_yes_no_radio(self, layout):
        """Добавляет переключатель Да/Нет"""
        button_group = QButtonGroup(layout.parentWidget())
        yes_radio = QRadioButton("Да")
        yes_radio.setObjectName("yes_radio")
        no_radio = QRadioButton("Нет")
        no_radio.setObjectName("no_radio")
        button_group.addButton(yes_radio)
        button_group.addButton(no_radio)
        layout.addWidget(yes_radio)
        layout.addWidget(no_radio)

    def add_slider(self, layout, min_val, max_val, width=400):
        """Добавляет слайдер для оценки"""
        container = QWidget()
        v_layout = QVBoxLayout(container)
        v_layout.setSpacing(0)
        v_layout.setContentsMargins(0, 0, 0, 0)

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(1)
        slider.setSingleStep(1)
        slider.setFixedSize(width, 35)
        v_layout.addWidget(slider)

        labels_container = self.create_slider_labels(min_val, max_val, width)
        v_layout.addWidget(labels_container)

        layout.addWidget(container)

    def create_slider_labels(self, min_val, max_val, width):
        """Создает подписи для слайдера"""
        container = QWidget()
        container.setFixedWidth(width)
        h_layout = QHBoxLayout(container)
        h_layout.setSpacing(0)
        h_layout.setContentsMargins(6, 0, 6, 0)

        for i in range(min_val, max_val + 1):
            label = QLabel(str(i))
            label.setAlignment(Qt.AlignCenter)
            label.setFixedWidth(width // max_val)
            h_layout.addWidget(label)

        return container

    def add_text_edit(self, layout):
        """Добавляет поле для текстового ответа"""
        text_edit = QTextEdit()
        text_edit.setMaximumHeight(100)
        text_edit.setStyleSheet(self.get_text_edit_style())
        layout.addWidget(text_edit)

    def get_text_edit_style(self):
        """Возвращает стиль для текстового поля"""
        return f"""
            QTextEdit {{
                background-color: {self.main_window.theme.COLOR_BACKGROUND_1};
                border: 1px solid {self.main_window.theme.COLOR_BACKGROUND_3};
                border-radius: 5px;
                padding: 5px;
                max-width: 400px;
            }}
            QTextEdit:focus {{
                border: 1px solid {self.main_window.theme.COLOR_ACCENT_1};
            }}      
        """

    def show_add_questionary_dialog(self):
        """Показывает диалог добавления новой анкеты"""
        dialog = AddQuestionnaireDialog(self.db, self.user_id, self.role_id, self.main_window)
        if dialog.exec() == QDialog.Accepted:
            self.load_user_templates()
            self.main_window.show_success_message("Шаблон успешно создан!")

    def clear_layout(self, layout):
        """Очищает компоновку от виджетов"""
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_layout(item.layout())

    def return_to_questions_page(self):
        """Возвращает на страницу со списком анкет"""
        self.clear_data()
        self.ui.mainPages.setCurrentWidget(self.ui.questionsPage)

    def clear_data(self):
        """Очищает поля ввода данных кандидата"""
        self.ui.cNameLineEdit.clear()
        self.ui.cSernameLineEdit.clear()
        self.ui.cPatronimicLineEdit.clear()
        self.ui.cEmailLineEdit.clear()
        self.ui.cPhoneLineEdit.clear()
        self.ui.cLinkLineEdit.clear()

    def save_questionnaire_results(self):
        """Сохраняет результаты заполнения анкеты"""
        try:
            candidate_data = self.get_candidate_data()
            if not self.validate_candidate_data(candidate_data):
                return

            candidate_id = self.db.add_candidate(**candidate_data)
            if not candidate_id:
                QMessageBox.warning(self.main_window, "Ошибка", "Не удалось добавить кандидата")
                return

            questionnaire = self.get_current_questionnaire()
            if not questionnaire:
                QMessageBox.critical(self.main_window, "Ошибка", "Не удалось определить анкету")
                return

            interview_id = self.db.add_interview(
                questionnaire_id=questionnaire['id'],
                interviewer_id=self.user_id,
                candidate_id=candidate_id,
                status_id=2
            )

            if not interview_id:
                QMessageBox.critical(self.main_window, "Ошибка", "Не удалось создать интервью")
                return

            total_score = self.save_answers(interview_id, questionnaire['id'])
            self.show_results(total_score, questionnaire['id'])

        except Exception as e:
            self.main_window.show_error_message(f"Ошибка при сохранении: {str(e)}")

    def get_candidate_data(self):
        """Возвращает данные кандидата из формы"""
        return {
            'first_name': self.ui.cNameLineEdit.text().strip(),
            'last_name': self.ui.cSernameLineEdit.text().strip(),
            'patronimic': self.ui.cPatronimicLineEdit.text().strip(),
            'email': self.ui.cEmailLineEdit.text().strip(),
            'phone': self.ui.cPhoneLineEdit.text().strip(),
            'resume_link': self.ui.cLinkLineEdit.text().strip(),
            'status_id': 2
        }

    def validate_candidate_data(self, data):
        """Проверяет обязательные поля кандидата"""
        if not data['first_name'] or not data['last_name'] or not data['email'] or not data['phone']:
            QMessageBox.warning(self.main_window, "Ошибка",
                                "Заполните обязательные поля (имя, фамилия, email, телефон)")
            return False
        return True

    def get_current_questionnaire(self):
        """Возвращает текущую анкету"""
        questionnaire_title = self.ui.questionnaryNameLabel.text().strip()
        return self.db.execute_query(
            "SELECT id FROM Questionnaires WHERE title = %s",
            (questionnaire_title,),
            fetch_all=False
        )

    def save_answers(self, interview_id, questionnaire_id):
        """Сохраняет ответы на вопросы анкеты"""
        questions = self.db.get_questions_for_questionnaire(questionnaire_id)
        if not questions:
            QMessageBox.critical(self.main_window, "Ошибка", "Не найдены вопросы для анкеты")
            return 0

        question_widgets = self.get_question_widgets()
        total_score = 0

        for i, question in enumerate(questions):
            if i >= len(question_widgets):
                continue

            answer_data = self.get_answer_data(question_widgets[i], question)
            if answer_data:
                value_numeric = answer_data.get('value_numeric', 0)
                if value_numeric is not None:
                    total_score += value_numeric

                success = self.db.add_answer(
                    interview_id=interview_id,
                    question_id=question['id'],
                    value_numeric=value_numeric,
                    selected_options=answer_data.get('selected_options'),
                    text_answer=answer_data.get('text_answer')
                )
                if success:
                    print(f"Не удалось сохранить ответ на вопрос {question['id']}")

        return total_score

    def get_question_widgets(self):
        """Возвращает список виджетов вопросов"""
        widgets = []
        layout = self.ui.questionsBlock.layout()
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget:
                widgets.append(widget)
        return widgets

    def get_answer_data(self, widget, question):
        """Возвращает данные ответа на вопрос"""
        answer_type = question['answer_type_id']

        if answer_type == 1:  # Множественный выбор
            return self.process_checkbox_answer(widget, question)
        elif answer_type == 2:  # Одиночный выбор
            return self.process_radio_answer(widget, question)
        elif answer_type in (3, 4):  # Шкала
            return self.process_slider_answer(widget, question)
        elif answer_type == 5:  # Да/Нет
            return self.process_yes_no_answer(widget, question)
        else:  # Текстовый ответ
            return self.process_text_answer(widget)

    def process_checkbox_answer(self, widget, question):
        """Обрабатывает ответ с множественным выбором"""
        options = self.db.get_options_for_question(question['id'])
        selected_ids = []
        sum_scores = 0

        for option in options:
            for child in widget.findChildren(QCheckBox):
                if child.text() == option['text'] and child.isChecked():
                    selected_ids.append(option['id'])
                    sum_scores += option['score']

        if selected_ids:
            return {
                'value_numeric': question['weight'] * sum_scores,
                'selected_options': str(selected_ids),
                'text_answer': None
            }
        return {'value_numeric': 0}

    def process_radio_answer(self, widget, question):
        """Обрабатывает ответ с одиночным выбором"""
        for child in widget.findChildren(QRadioButton):
            if child.isChecked():
                option = self.db.execute_query(
                    "SELECT id, score FROM QuestionOptions WHERE question_id = %s AND text = %s",
                    (question['id'], child.text()),
                    fetch_all=False
                )
                if option:
                    return {
                        'value_numeric': question['weight'] * option['score'],
                        'selected_options': str([option['id']]),
                        'text_answer': None
                    }
        return {'value_numeric': 0}

    def process_slider_answer(self, widget, question):
        """Обрабатывает ответ со шкалой"""
        slider = widget.findChild(QSlider)
        if slider:
            return {
                'value_numeric': question['weight'] * slider.value(),
                'selected_options': None,
                'text_answer': None
            }
        return {}

    def process_yes_no_answer(self, widget, question):
        """Обрабатывает ответ Да/Нет"""
        for child in widget.findChildren(QRadioButton):
            if child.isChecked():
                value = 1 if child.text() == "Да" else 0
                return {
                    'value_numeric': question['weight'] * value,
                    'selected_options': f'["{child.text()}"]',
                    'text_answer': None
                }
        return {'value_numeric': 0}

    def process_text_answer(self, widget):
        """Обрабатывает текстовый ответ"""
        text_edit = widget.findChild(QTextEdit)
        if text_edit and text_edit.toPlainText().strip():
            return {
                'value_numeric': 0,
                'selected_options': None,
                'text_answer': text_edit.toPlainText().strip()
            }
        return {'value_numeric': 0}

    def show_results(self, total_score, questionnaire_id):
        """Показывает результаты тестирования"""
        max_score = self.db.get_max_score_for_questionnaire(questionnaire_id)
        percentage = (total_score / max_score) * 100 if max_score else 0

        if percentage < 50:
            rating = "Низкий результат"
        elif percentage < 80:
            rating = "Средний результат"
        else:
            rating = "Высокий результат"

        self.main_window.show_success_message(
            f"Результаты успешно сохранены!\n"
            f"Суммарный балл: {round(total_score, 2)} из {max_score}\n"
            f"Оценка: {rating} ({round(percentage)}%)"
        )

        self.clear_data()
        self.return_to_questions_page()