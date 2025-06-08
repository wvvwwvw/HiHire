import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        """Инициализирует подключение к базе данных"""
        self.connection = None
        self.connect()

    def connect(self):
        """Устанавливает соединение с базой данных"""
        try:
            self.connection = mysql.connector.connect(
                host="MySQL-8.2",
                user="root",
                password="root",
                database="HiHireDB"
            )
            if self.connection.is_connected():
                print("Успешное подключение к базе данных")
        except Error as e:
            print(f"Ошибка подключения к MySQL: {e}")

    def disconnect(self):
        """Закрывает соединение с базой данных"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Соединение с MySQL закрыто")

    def execute_query(self, query, params=None, fetch_all=True, return_lastrowid=False):
        """Выполняет SQL-запрос и возвращает результат"""
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())

            result = cursor.fetchall() if fetch_all else cursor.fetchone()
            self.connection.commit()

            return cursor.lastrowid if return_lastrowid else result
        except Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            self.connection.rollback()
            return None
        finally:
            if cursor:
                cursor.close()

    def get_questionnaires(self, is_public=None, user_id=None, limit=None):
        """Возвращает список анкет с фильтрами"""
        query = """
        SELECT id, position_id, title, description, created_by, is_public, created_at 
        FROM Questionnaires 
        WHERE (%s IS NULL OR is_public = %s)
        AND (%s IS NULL OR created_by = %s)
        ORDER BY id ASC
        """
        params = [is_public, is_public, user_id, user_id]

        if limit:
            query += " LIMIT %s"
            params.append(limit)

        return self.execute_query(query, params)

    def get_questions_for_questionnaire(self, questionnaire_id):
        """Возвращает вопросы для указанной анкеты"""
        query = """
        SELECT q.id, q.text, q.weight, q.answer_type_id, q.category_id,
               at.name as answer_type_name
        FROM Questions q
        JOIN QuestionnaireQuestions qq ON q.id = qq.question_id
        JOIN AnswerTypes at ON q.answer_type_id = at.id
        WHERE qq.questionnaire_id = %s
        """
        return self.execute_query(query, (questionnaire_id,))

    def get_max_score_for_questionnaire(self, questionnaire_id):
        """Возвращает максимальный балл для анкеты"""
        query = """
        SELECT IFNULL(SUM(
            CASE q.answer_type_id
                WHEN 1 THEN q.weight * IFNULL((SELECT SUM(score) FROM QuestionOptions WHERE question_id = q.id), 0)
                WHEN 2 THEN q.weight * IFNULL((SELECT MAX(score) FROM QuestionOptions WHERE question_id = q.id), 0)
                WHEN 3 THEN q.weight * 5
                WHEN 4 THEN q.weight * 10
                WHEN 5 THEN q.weight * 1
                ELSE 0
            END
        ), 0) AS max_score
        FROM Questions q
        JOIN QuestionnaireQuestions qq ON q.id = qq.question_id
        WHERE qq.questionnaire_id = %s
        """
        result = self.execute_query(query, (questionnaire_id,), fetch_all=False)
        return result.get('max_score', 0) if result else 0

    def get_options_for_question(self, question_id):
        """Возвращает варианты ответов для вопроса"""
        query = """
        SELECT id, text, score
        FROM QuestionOptions
        WHERE question_id = %s
        ORDER BY id
        """
        return self.execute_query(query, (question_id,))

    def get_answer_types(self):
        """Возвращает все типы ответов"""
        return self.execute_query("SELECT id, name FROM AnswerTypes")

    def get_positions(self):
        """Возвращает список должностей"""
        return self.execute_query("SELECT id, name FROM Positions")

    def add_candidate(self, first_name, last_name, patronimic, email, phone, resume_link, status_id):
        """Добавляет нового кандидата в базу данных"""
        query = """
        INSERT INTO Candidates (first_name, last_name, patronimic, email, phone, resume_link, status_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        return self.execute_query(query, (first_name, last_name, patronimic, email, phone, resume_link, status_id),
                                  fetch_all=False, return_lastrowid=True)

    def add_interview(self, questionnaire_id, interviewer_id, candidate_id, status_id):
        """Добавляет новое интервью в базу данных"""
        query = """
        INSERT INTO Interviews (questionnaire_id, interviewer_id, candidate_id, status_id)
        VALUES (%s, %s, %s, %s)
        """
        return self.execute_query(query, (questionnaire_id, interviewer_id, candidate_id, status_id),
                                  fetch_all=False, return_lastrowid=True)

    def add_answer(self, interview_id, question_id, value_numeric=None, selected_options=None, text_answer=None):
        """Добавляет ответ на вопрос"""
        query = """
        INSERT INTO Answers (interview_id, question_id, value_numeric, selected_options, text_answer)
        VALUES (%s, %s, %s, %s, %s)
        """
        return bool(self.execute_query(query, (interview_id, question_id, value_numeric, selected_options, text_answer),
                                       fetch_all=False))

    def get_full_interview_data(self, interview_id):
        """Получает полные данные об интервью для экспорта"""
        query = """
        SELECT 
            i.id as interview_id,
            i.created_at as interview_date,
            q.title as questionnaire_title,
            p.name as position_name,
            c.first_name, c.last_name, c.patronimic, c.email, c.phone, c.resume_link,
            s.name as status_name,
            q2.text as question_text,
            q2.weight as question_weight,
            at.name as answer_type,
            cat.name as category_name,
            a.value_numeric, a.selected_options, a.text_answer
        FROM Interviews i
        JOIN Questionnaires q ON i.questionnaire_id = q.id
        JOIN Positions p ON q.position_id = p.id
        JOIN Candidates c ON i.candidate_id = c.id
        JOIN Statuses s ON i.status_id = s.id
        JOIN QuestionnaireQuestions qq ON q.id = qq.questionnaire_id
        JOIN Questions q2 ON qq.question_id = q2.id
        JOIN AnswerTypes at ON q2.answer_type_id = at.id
        JOIN Categories cat ON q2.category_id = cat.id
        LEFT JOIN Answers a ON i.id = a.interview_id AND q2.id = a.question_id
        WHERE i.id = %s
        """
        return self.execute_query(query, (interview_id,))

    def import_interview_data(self, data):
        """Импортирует данные интервью из словаря"""
        try:
            candidate_id = self.add_candidate(
                data['first_name'],
                data['last_name'],
                data.get('patronimic'),
                data['email'],
                data['phone'],
                data['resume_link'],
                data['status_id']
            )

            interview_id = self.add_interview(
                data['questionnaire_id'],
                data['interviewer_id'],
                candidate_id,
                data['status_id']
            )

            for answer in data['answers']:
                self.add_answer(
                    interview_id,
                    answer['question_id'],
                    answer.get('value_numeric'),
                    answer.get('selected_options'),
                    answer.get('text_answer')
                )

            return interview_id
        except Error as e:
            print(f"Ошибка при импорте данных интервью: {e}")
            return None