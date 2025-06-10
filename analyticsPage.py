from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QDateEdit, QGridLayout, QSizePolicy, QScrollArea, QFrame
from PySide6.QtCore import Qt, QDate
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QBarSeries, QBarSet, QValueAxis, QBarCategoryAxis, \
    QLineSeries
from connect_to_database import Database
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class AnalyticsPage:
    def __init__(self, ui, main_window):
        self.ui = ui
        self.main_window = main_window
        self.db = Database()
        self.user_id = None
        self.role_id = None

        self.connect_filter_signals()
        self.init_charts()

    def connect_filter_signals(self):
        """Подключает сигналы фильтров"""
        self.ui.comboBox.currentIndexChanged.connect(self.update_charts)
        self.ui.comboBox_2.currentIndexChanged.connect(self.update_charts)
        self.ui.dateEdit.dateChanged.connect(self.update_charts)
        self.ui.dateEdit_2.dateChanged.connect(self.update_charts)

    def init_analytic(self, role_id, user_id):
        """Инициализирует страницу аналитики"""
        self.role_id = role_id
        self.user_id = user_id
        self.init_filters()
        self.update_charts()

    def init_filters(self):
        """Инициализирует фильтры со значениями по умолчанию"""
        positions = self.db.execute_query("SELECT id, name FROM Positions")
        self.ui.comboBox.clear()
        self.ui.comboBox.addItem("Все должности", None)
        for position in positions:
            self.ui.comboBox.addItem(position['name'], position['id'])

        questionnaires = self.db.execute_query("SELECT id, title FROM Questionnaires WHERE created_by = %s OR is_public = 1", (self.user_id,))
        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItem("Все шаблоны", None)
        for q in questionnaires:
            self.ui.comboBox_2.addItem(q['title'], q['id'])

        today = QDate.currentDate()
        self.ui.dateEdit.setDate(today.addDays(-30))
        self.ui.dateEdit_2.setDate(today)

    def init_charts(self):
        """Инициализирует все графики"""
        self.charts_container = QWidget()
        self.grid_layout = QGridLayout(self.charts_container)
        self.grid_layout.setSpacing(10)
        self.grid_layout.setContentsMargins(5, 5, 5, 5)

        self.candidates_pie_chart = self.create_pie_chart()
        self.category_bar_chart = self.create_bar_chart()
        self.questionnaire_bar_chart = self.create_bar_chart()
        self.tools_pie_chart = self.create_pie_chart()
        self.interviews_line_chart = self.create_line_chart()
        self.employees_pie_chart = self.create_pie_chart()

        for chart in [self.candidates_pie_chart, self.category_bar_chart,
                     self.questionnaire_bar_chart, self.tools_pie_chart,
                     self.interviews_line_chart, self.employees_pie_chart]:
            chart.setMinimumHeight(350)

        self.grid_layout.addWidget(self.candidates_pie_chart, 0, 0)
        self.grid_layout.addWidget(self.category_bar_chart, 0, 1)
        self.grid_layout.addWidget(self.questionnaire_bar_chart, 1, 0)
        self.grid_layout.addWidget(self.tools_pie_chart, 1, 1)
        self.grid_layout.addWidget(self.interviews_line_chart, 2, 0)
        self.grid_layout.addWidget(self.employees_pie_chart, 2, 1)

        for i in range(3):
            self.grid_layout.setRowStretch(i, 1)
        for j in range(2):
            self.grid_layout.setColumnStretch(j, 1)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.charts_container)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        layout = self.ui.widget_37.layout()
        if layout is not None:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().setParent(None)
        else:
            layout = QVBoxLayout(self.ui.widget_37)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)

        layout.addWidget(scroll_area)

    def create_pie_chart(self):
        """Создание круговой диаграммы"""
        fig, ax = plt.subplots(figsize=(4, 3))
        fig.subplots_adjust(left=0.15, right=0.85, top=0.9, bottom=0.25)
        canvas = FigureCanvas(fig)
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        return canvas

    def create_bar_chart(self):
        """Создание столбчатой диаграммы"""
        fig, ax = plt.subplots(figsize=(4, 3))
        fig.subplots_adjust(left=0.15, right=0.85, top=0.9, bottom=0.25)
        canvas = FigureCanvas(fig)
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        return canvas

    def create_line_chart(self):
        """Создание линейного графика"""
        fig, ax = plt.subplots(figsize=(4, 3))
        fig.subplots_adjust(left=0.15, right=0.85, top=0.9, bottom=0.25)
        canvas = FigureCanvas(fig)
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        return canvas

    def update_charts(self):
        """Обновляет все графики на основе текущих фильтров"""
        filters = self.get_current_filters()

        self.update_candidates_status_chart(filters)
        self.update_category_scores_chart(filters)
        self.update_questionnaire_scores_chart(filters)
        self.update_top_tools_chart(filters)
        self.update_interviews_by_day_chart(filters)
        self.update_employees_status_chart()

    def get_current_filters(self):
        """Возвращает текущие значения фильтров"""
        return {
            'position_id': self.ui.comboBox.currentData(),
            'questionnaire_id': self.ui.comboBox_2.currentData(),
            'start_date': self.ui.dateEdit.date().toString("yyyy-MM-dd"),
            'end_date': self.ui.dateEdit_2.date().toString("yyyy-MM-dd")
        }

    def update_candidates_status_chart(self, filters):
        """Обновляет диаграмму статусов кандидатов"""
        query = """
        SELECT s.name, COUNT(c.id) as count
        FROM Candidates c
        JOIN Statuses s ON c.status_id = s.id
        JOIN Interviews i ON c.id = i.candidate_id
        WHERE c.created_at BETWEEN %s AND %s
        """
        params = [filters['start_date'], filters['end_date']]

        if self.role_id != 1:
            query += " AND i.interviewer_id = %s"
            params.append(self.user_id)

        query += " GROUP BY s.name"

        data = self.db.execute_query(query, params)

        self.candidates_pie_chart.figure.clear()
        ax = self.candidates_pie_chart.figure.add_subplot(111)
        if not data:
            ax.text(0.5, 0.5, 'Нет данных', ha='center', va='center')
            self.candidates_pie_chart.draw()
            return

        labels = [item['name'] for item in data]
        sizes = [item['count'] for item in data]
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Статусы кандидатов')
        self.candidates_pie_chart.draw()

    def update_category_scores_chart(self, filters):
        """Обновляет диаграмму средних баллов по категориям"""
        query = """
        SELECT cat.name, 
               AVG(a.value_numeric) as avg_score,
               MAX(q.weight * 
                   CASE q.answer_type_id
                       WHEN 1 THEN (SELECT SUM(score) FROM QuestionOptions WHERE question_id = q.id)
                       WHEN 2 THEN (SELECT MAX(score) FROM QuestionOptions WHERE question_id = q.id)
                       WHEN 3 THEN 5
                       WHEN 4 THEN 10
                       WHEN 5 THEN 1
                       ELSE 0
                   END) as max_score
        FROM Answers a
        JOIN Questions q ON a.question_id = q.id
        JOIN Categories cat ON q.category_id = cat.id
        JOIN Interviews i ON a.interview_id = i.id
        WHERE i.created_at BETWEEN %s AND %s
        """
        params = [filters['start_date'], filters['end_date']]

        if self.role_id != 1:
            query += " AND i.interviewer_id = %s"
            params.append(self.user_id)

        if filters['questionnaire_id']:
            query += " AND i.questionnaire_id = %s"
            params.append(filters['questionnaire_id'])

        query += " GROUP BY cat.name"

        data = self.db.execute_query(query, params)

        self.category_bar_chart.figure.clear()
        ax = self.category_bar_chart.figure.add_subplot(111)

        if not data:
            ax.text(0.5, 0.5, 'Нет данных', ha='center', va='center')
            self.category_bar_chart.draw()
            return

        categories = [item['name'] for item in data]
        avg_scores = [float(item['avg_score']) for item in data]
        max_scores = [float(item['max_score']) for item in data]

        bar_width = 0.35
        index = range(len(categories))

        bars1 = ax.bar(index, avg_scores, bar_width, label='Средний балл')
        bars2 = ax.bar([i + bar_width for i in index], max_scores, bar_width, label='Максимальный балл')

        ax.set_xlabel('Категории')
        ax.set_ylabel('Баллы')
        ax.set_title('Средний балл по категориям')
        ax.set_xticks([i + bar_width / 2 for i in index])
        ax.set_xticklabels(categories, rotation=10, ha='right')
        ax.legend()

        self.add_value_labels(ax, bars1)
        self.add_value_labels(ax, bars2)

        self.category_bar_chart.figure.tight_layout()
        self.category_bar_chart.draw()

    def add_value_labels(self, ax, bars):
        """Добавляет подписи значений на столбцы диаграммы"""
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height,
                    f'{height:.1f}',
                    ha='center', va='bottom')

    def update_questionnaire_scores_chart(self, filters):
        """Обновляет диаграмму средних баллов по анкетам"""
        query = """
        SELECT q.title, 
               AVG(COALESCE(a.value_numeric, 0)) as avg_score,
               MAX(qs.weight * 
                   CASE qs.answer_type_id
                       WHEN 1 THEN (SELECT COALESCE(SUM(score), 0) FROM QuestionOptions WHERE question_id = qs.id)
                       WHEN 2 THEN (SELECT COALESCE(MAX(score), 0) FROM QuestionOptions WHERE question_id = qs.id)
                       WHEN 3 THEN 5
                       WHEN 4 THEN 10
                       WHEN 5 THEN 1
                       ELSE 0
                   END) as max_score
        FROM Answers a
        JOIN Questions qs ON a.question_id = qs.id
        JOIN QuestionnaireQuestions qq ON qs.id = qq.question_id
        JOIN Questionnaires q ON qq.questionnaire_id = q.id
        JOIN Interviews i ON a.interview_id = i.id
        WHERE i.created_at BETWEEN %s AND %s
        """
        params = [filters['start_date'], filters['end_date']]

        if self.role_id != 1:
            query += " AND i.interviewer_id = %s"
            params.append(self.user_id)

        if filters['position_id']:
            query += " AND q.position_id = %s"
            params.append(filters['position_id'])

        query += " GROUP BY q.title"

        data = self.db.execute_query(query, params)

        self.questionnaire_bar_chart.figure.clear()
        ax = self.questionnaire_bar_chart.figure.add_subplot(111)

        if not data:
            ax.text(0.5, 0.5, 'Нет данных', ha='center', va='center')
            self.questionnaire_bar_chart.draw()
            return

        questionnaires = [item['title'] for item in data]
        avg_scores = [float(item['avg_score']) for item in data]
        max_scores = [float(item['max_score']) for item in data]

        bar_width = 0.35
        index = range(len(questionnaires))

        bars1 = ax.bar(index, avg_scores, bar_width, label='Средний балл')
        bars2 = ax.bar([i + bar_width for i in index], max_scores, bar_width, label='Максимальный балл')

        ax.set_xlabel('Шаблоны анкет')
        ax.set_ylabel('Баллы')
        ax.set_title('Средний балл по шаблонам')
        ax.set_xticks([i + bar_width / 2 for i in index])
        ax.set_xticklabels(questionnaires, rotation=10, ha='right')
        ax.legend()

        self.add_value_labels(ax, bars1)
        self.add_value_labels(ax, bars2)

        self.questionnaire_bar_chart.figure.tight_layout()
        self.questionnaire_bar_chart.draw()

    def update_top_tools_chart(self, filters):
        """Обновляет диаграмму топ-5 инструментов"""
        query = """
        SELECT opt.text, COUNT(a.id) as count
        FROM Answers a
        JOIN QuestionOptions opt ON JSON_CONTAINS(a.selected_options, CAST(opt.id AS JSON), '$')
        JOIN Questions q ON a.question_id = q.id
        JOIN Categories cat ON q.category_id = cat.id
        JOIN Interviews i ON a.interview_id = i.id
        WHERE cat.name = 'Инструменты'
        AND i.created_at BETWEEN %s AND %s
        """
        params = [filters['start_date'], filters['end_date']]

        if self.role_id != 1:
            query += " AND i.interviewer_id = %s"
            params.append(self.user_id)

        query += " GROUP BY opt.text ORDER BY count DESC LIMIT 5"

        data = self.db.execute_query(query, params)

        self.tools_pie_chart.figure.clear()
        ax = self.tools_pie_chart.figure.add_subplot(111)
        if not data:
            ax.text(0.5, 0.5, 'Нет данных', ha='center', va='center')
            self.tools_pie_chart.draw()
            return

        labels = [item['text'] for item in data]
        counts = [item['count'] for item in data]
        ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Топ 5 инструментов')
        self.tools_pie_chart.draw()

    def update_interviews_by_day_chart(self, filters):
        """Обновляет график интервью по дням"""
        query = """
        SELECT DATE(i.created_at) as date, COUNT(i.id) as count
        FROM Interviews i
        WHERE i.created_at BETWEEN %s AND %s
        """
        params = [filters['start_date'], filters['end_date']]

        if self.role_id != 1:
            query += " AND i.interviewer_id = %s"
            params.append(self.user_id)

        query += " GROUP BY DATE(i.created_at) ORDER BY date"

        data = self.db.execute_query(query, params)

        self.interviews_line_chart.figure.clear()
        ax = self.interviews_line_chart.figure.add_subplot(111)
        if not data:
            ax.text(0.5, 0.5, 'Нет данных', ha='center', va='center')
            self.interviews_line_chart.draw()
            return

        dates = [item['date'].strftime('%Y-%m-%d') for item in data]
        counts = [item['count'] for item in data]
        ax.plot(dates, counts, marker='o')
        ax.set_xlabel('Дата')
        ax.set_ylabel('Количество интервью')
        ax.set_title('Интервью по дням')
        ax.grid(True)
        plt.setp(ax.get_xticklabels(), rotation=5, ha='right')
        self.interviews_line_chart.draw()

    def update_employees_status_chart(self):
        """Обновляет диаграмму статусов сотрудников"""
        query = """
        SELECT s.name, COUNT(e.id) as count
        FROM Employees e
        JOIN Statuses s ON e.status_id = s.id
        GROUP BY s.name
        """

        data = self.db.execute_query(query)

        self.employees_pie_chart.figure.clear()
        ax = self.employees_pie_chart.figure.add_subplot(111)
        if not data:
            ax.text(0.5, 0.5, 'Нет данных', ha='center', va='center')
            self.employees_pie_chart.draw()
            return

        labels = [item['name'] for item in data]
        sizes = [item['count'] for item in data]

        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Статусы сотрудников')

        self.employees_pie_chart.draw()