-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Хост: MySQL-8.2
-- Время создания: Июн 09 2025 г., 02:57
-- Версия сервера: 8.2.0
-- Версия PHP: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `HiHireDB`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Answers`
--

CREATE TABLE `Answers` (
  `id` int NOT NULL,
  `interview_id` int NOT NULL,
  `question_id` int NOT NULL,
  `value_numeric` int DEFAULT NULL,
  `selected_options` json DEFAULT NULL,
  `text_answer` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `AnswerTypes`
--

CREATE TABLE `AnswerTypes` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Candidates`
--

CREATE TABLE `Candidates` (
  `id` int NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `patronimic` varchar(100) DEFAULT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` varchar(20) NOT NULL,
  `resume_link` varchar(255) NOT NULL,
  `status_id` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Categories`
--

CREATE TABLE `Categories` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Emails`
--

CREATE TABLE `Emails` (
  `id` int NOT NULL,
  `sender_id` int NOT NULL,
  `candidate_id` int NOT NULL,
  `subject` varchar(50) NOT NULL,
  `message` text NOT NULL,
  `sent_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Employees`
--

CREATE TABLE `Employees` (
  `id` int NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `patronimic` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `position_id` int NOT NULL,
  `hire_date` date NOT NULL,
  `fire_date` date DEFAULT NULL,
  `status_id` int NOT NULL,
  `skills` varchar(500) DEFAULT NULL,
  `organization_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Interviews`
--

CREATE TABLE `Interviews` (
  `id` int NOT NULL,
  `questionnaire_id` int NOT NULL,
  `interviewer_id` int NOT NULL,
  `candidate_id` int NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Organizations`
--

CREATE TABLE `Organizations` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `status_id` int NOT NULL,
  `description` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Positions`
--

CREATE TABLE `Positions` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `QuestionnaireQuestions`
--

CREATE TABLE `QuestionnaireQuestions` (
  `questionnaire_id` int NOT NULL,
  `question_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Questionnaires`
--

CREATE TABLE `Questionnaires` (
  `id` int NOT NULL,
  `position_id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text,
  `created_by` int NOT NULL,
  `is_public` tinyint(1) NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `QuestionOptions`
--

CREATE TABLE `QuestionOptions` (
  `id` int NOT NULL,
  `question_id` int NOT NULL,
  `text` varchar(255) NOT NULL,
  `score` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Questions`
--

CREATE TABLE `Questions` (
  `id` int NOT NULL,
  `text` text NOT NULL,
  `weight` int DEFAULT '1',
  `answer_type_id` int NOT NULL,
  `category_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Roles`
--

CREATE TABLE `Roles` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Statuses`
--

CREATE TABLE `Statuses` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Users`
--

CREATE TABLE `Users` (
  `id` int NOT NULL,
  `login` varchar(100) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `salt` char(32) NOT NULL,
  `work_email_password` varchar(50) NOT NULL,
  `employee_id` int NOT NULL,
  `last_entry` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `role_id` int NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `avatar` longblob
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `Answers`
--
ALTER TABLE `Answers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `interview_id` (`interview_id`),
  ADD KEY `question_id` (`question_id`);

--
-- Индексы таблицы `AnswerTypes`
--
ALTER TABLE `AnswerTypes`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `Candidates`
--
ALTER TABLE `Candidates`
  ADD PRIMARY KEY (`id`),
  ADD KEY `status_id` (`status_id`);

--
-- Индексы таблицы `Categories`
--
ALTER TABLE `Categories`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `Emails`
--
ALTER TABLE `Emails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `status_id` (`status_id`),
  ADD KEY `candidate_id` (`candidate_id`),
  ADD KEY `sender_id` (`sender_id`);

--
-- Индексы таблицы `Employees`
--
ALTER TABLE `Employees`
  ADD PRIMARY KEY (`id`),
  ADD KEY `organization_id` (`organization_id`),
  ADD KEY `position_id` (`position_id`),
  ADD KEY `status_id` (`status_id`);

--
-- Индексы таблицы `Interviews`
--
ALTER TABLE `Interviews`
  ADD PRIMARY KEY (`id`),
  ADD KEY `questionnaire_id` (`questionnaire_id`),
  ADD KEY `conducted_by` (`interviewer_id`),
  ADD KEY `candidate_id` (`candidate_id`),
  ADD KEY `status` (`status_id`);

--
-- Индексы таблицы `Organizations`
--
ALTER TABLE `Organizations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `status_id` (`status_id`);

--
-- Индексы таблицы `Positions`
--
ALTER TABLE `Positions`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `QuestionnaireQuestions`
--
ALTER TABLE `QuestionnaireQuestions`
  ADD PRIMARY KEY (`questionnaire_id`,`question_id`),
  ADD KEY `question_id` (`question_id`);

--
-- Индексы таблицы `Questionnaires`
--
ALTER TABLE `Questionnaires`
  ADD PRIMARY KEY (`id`),
  ADD KEY `created_by` (`created_by`),
  ADD KEY `position_id` (`position_id`);

--
-- Индексы таблицы `QuestionOptions`
--
ALTER TABLE `QuestionOptions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `question_id` (`question_id`);

--
-- Индексы таблицы `Questions`
--
ALTER TABLE `Questions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `answer_type_id` (`answer_type_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Индексы таблицы `Roles`
--
ALTER TABLE `Roles`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `Statuses`
--
ALTER TABLE `Statuses`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login` (`login`),
  ADD UNIQUE KEY `employee_id` (`employee_id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `Answers`
--
ALTER TABLE `Answers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `AnswerTypes`
--
ALTER TABLE `AnswerTypes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Candidates`
--
ALTER TABLE `Candidates`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Categories`
--
ALTER TABLE `Categories`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Emails`
--
ALTER TABLE `Emails`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Employees`
--
ALTER TABLE `Employees`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Interviews`
--
ALTER TABLE `Interviews`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Organizations`
--
ALTER TABLE `Organizations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Positions`
--
ALTER TABLE `Positions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Questionnaires`
--
ALTER TABLE `Questionnaires`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `QuestionOptions`
--
ALTER TABLE `QuestionOptions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Questions`
--
ALTER TABLE `Questions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Roles`
--
ALTER TABLE `Roles`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Statuses`
--
ALTER TABLE `Statuses`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `Answers`
--
ALTER TABLE `Answers`
  ADD CONSTRAINT `answers_ibfk_1` FOREIGN KEY (`interview_id`) REFERENCES `Interviews` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `answers_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `Questions` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `Candidates`
--
ALTER TABLE `Candidates`
  ADD CONSTRAINT `candidates_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `Statuses` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `Emails`
--
ALTER TABLE `Emails`
  ADD CONSTRAINT `emails_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `Statuses` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `emails_ibfk_2` FOREIGN KEY (`candidate_id`) REFERENCES `Candidates` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `emails_ibfk_3` FOREIGN KEY (`sender_id`) REFERENCES `Users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `Employees`
--
ALTER TABLE `Employees`
  ADD CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`organization_id`) REFERENCES `Organizations` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`position_id`) REFERENCES `Positions` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `employees_ibfk_3` FOREIGN KEY (`status_id`) REFERENCES `Statuses` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `Interviews`
--
ALTER TABLE `Interviews`
  ADD CONSTRAINT `interviews_ibfk_1` FOREIGN KEY (`questionnaire_id`) REFERENCES `Questionnaires` (`id`),
  ADD CONSTRAINT `interviews_ibfk_2` FOREIGN KEY (`interviewer_id`) REFERENCES `Users` (`id`),
  ADD CONSTRAINT `interviews_ibfk_3` FOREIGN KEY (`candidate_id`) REFERENCES `Candidates` (`id`),
  ADD CONSTRAINT `interviews_ibfk_4` FOREIGN KEY (`status_id`) REFERENCES `Statuses` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `Organizations`
--
ALTER TABLE `Organizations`
  ADD CONSTRAINT `organizations_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `Statuses` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `QuestionnaireQuestions`
--
ALTER TABLE `QuestionnaireQuestions`
  ADD CONSTRAINT `questionnairequestions_ibfk_1` FOREIGN KEY (`questionnaire_id`) REFERENCES `Questionnaires` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `questionnairequestions_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `Questions` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `Questionnaires`
--
ALTER TABLE `Questionnaires`
  ADD CONSTRAINT `questionnaires_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `Users` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `questionnaires_ibfk_2` FOREIGN KEY (`position_id`) REFERENCES `Positions` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `QuestionOptions`
--
ALTER TABLE `QuestionOptions`
  ADD CONSTRAINT `questionoptions_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `Questions` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `Questions`
--
ALTER TABLE `Questions`
  ADD CONSTRAINT `questions_ibfk_2` FOREIGN KEY (`answer_type_id`) REFERENCES `AnswerTypes` (`id`),
  ADD CONSTRAINT `questions_ibfk_3` FOREIGN KEY (`category_id`) REFERENCES `Categories` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `Users`
--
ALTER TABLE `Users`
  ADD CONSTRAINT `users_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `Roles` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `users_ibfk_3` FOREIGN KEY (`employee_id`) REFERENCES `Employees` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
