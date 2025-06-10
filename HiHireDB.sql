-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Хост: MySQL-8.2
-- Время создания: Июн 10 2025 г., 18:00
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

DELIMITER $$
--
-- Процедуры
--
CREATE DEFINER=`root`@`%` PROCEDURE `AuthenticateUser` (IN `p_login` VARCHAR(100), IN `p_password` VARCHAR(255))   BEGIN
    DECLARE v_user_id INT DEFAULT NULL;
    DECLARE v_role_id INT DEFAULT NULL;
    DECLARE v_salt CHAR(32) DEFAULT NULL;
    DECLARE v_stored_hash VARCHAR(255) DEFAULT NULL;
    DECLARE v_input_hash VARCHAR(255) DEFAULT NULL;
    DECLARE v_is_active TINYINT(1) DEFAULT 0;
    
    SELECT 
        id, 
        role_id, 
        salt, 
        password_hash,
        is_active
    INTO 
        v_user_id,
        v_role_id,
        v_salt,
        v_stored_hash,
        v_is_active
    FROM Users 
    WHERE login = p_login
    LIMIT 1;
    
    IF v_salt IS NOT NULL AND v_stored_hash IS NOT NULL THEN
        SET v_input_hash = SHA2(CONCAT(v_salt, p_password), 256);
        
        IF v_input_hash = v_stored_hash AND v_is_active = 1 THEN
            UPDATE Users 
            SET last_entry = CURRENT_TIMESTAMP 
            WHERE id = v_user_id;
            
            SELECT 
                v_user_id AS id,
                v_role_id AS role_id,
                'Авторизация прошла успешно' AS message;
        ELSE
            SELECT 
                NULL AS id,
                NULL AS role_id,
                CASE 
                    WHEN v_is_active = 0 THEN 'Аккаунт неактивен'
                    ELSE 'Неккоректные логин или пароль'
                END AS message;
        END IF;
    ELSE
        SELECT 
            NULL AS id,
            NULL AS role_id,
            'Неккоректные логин или пароль' AS message;
    END IF;
END$$

CREATE DEFINER=`root`@`%` PROCEDURE `CreateUserForEmployee` (IN `p_employee_id` INT, IN `p_login` VARCHAR(100), IN `p_password` VARCHAR(255), IN `p_role_id` INT, IN `p_work_email_password` VARCHAR(50))   BEGIN
    DECLARE v_salt CHAR(32);
    DECLARE v_password_hash VARCHAR(255);
    DECLARE v_employee_exists INT DEFAULT 0;
    DECLARE v_login_exists INT DEFAULT 0;
    
    SELECT COUNT(*) INTO v_employee_exists 
    FROM Employees 
    WHERE id = p_employee_id AND status_id IN (1, 6);
    
    SELECT COUNT(*) INTO v_login_exists 
    FROM Users 
    WHERE login = p_login;
    
    IF EXISTS (SELECT 1 FROM Users WHERE employee_id = p_employee_id) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'У этого сотрудника уже есть пользователь';
    ELSEIF v_employee_exists = 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Сотрудник не найден или неактивен';
    ELSEIF v_login_exists > 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Такой логин уже существует';
    ELSEIF p_login = '' OR p_password = '' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Логин и пароль не могут быть пустыми';
    ELSE

        SET v_salt = MD5(RAND());
        
        SET v_password_hash = SHA2(CONCAT(v_salt, p_password), 256);
        
        INSERT INTO Users (
            login, 
            password_hash, 
            salt, 
            work_email_password,
            employee_id, 
            role_id, 
            is_active, 
            last_entry
        ) VALUES (
            p_login,
            v_password_hash,
            v_salt,
            p_work_email_password,
            p_employee_id,
            p_role_id,
            1, 
            CURRENT_TIMESTAMP
        );
        
        SELECT LAST_INSERT_ID() AS new_user_id;
    END IF;
END$$

CREATE DEFINER=`root`@`%` PROCEDURE `ResetPassword` (IN `p_login` VARCHAR(100), IN `p_email` VARCHAR(100), IN `p_new_password` VARCHAR(255))   BEGIN
    DECLARE v_user_id INT DEFAULT NULL;
    DECLARE v_employee_id INT DEFAULT NULL;
    DECLARE v_employee_email VARCHAR(100) DEFAULT NULL;
    DECLARE v_salt CHAR(32) DEFAULT NULL;
    DECLARE v_new_hash VARCHAR(255) DEFAULT NULL;
    
    SELECT u.id, u.employee_id, u.salt, e.email 
    INTO v_user_id, v_employee_id, v_salt, v_employee_email
    FROM Users u
    JOIN Employees e ON u.employee_id = e.id
    WHERE u.login = p_login AND e.email = p_email
    LIMIT 1;
    
    IF v_user_id IS NOT NULL AND v_employee_email IS NOT NULL THEN
        IF v_salt IS NULL THEN
            SET v_salt = MD5(RAND());
        END IF;
        
        SET v_new_hash = SHA2(CONCAT(v_salt, p_new_password), 256);

        UPDATE Users 
        SET 
            password_hash = v_new_hash,
            salt = v_salt,
            last_entry = CURRENT_TIMESTAMP
        WHERE id = v_user_id;
        
        COMMIT;
        SELECT 1 AS success, 'Пароль успешно изменен' AS message;
    ELSE
    	ROLLBACK;
        SELECT 0 AS success, 'Пользователь с таким логином и email не найден' AS message;
    END IF;
END$$

DELIMITER ;

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

--
-- Дамп данных таблицы `Answers`
--

INSERT INTO `Answers` (`id`, `interview_id`, `question_id`, `value_numeric`, `selected_options`, `text_answer`) VALUES
(214, 47, 7, 2, '[30]', NULL),
(215, 47, 8, 9, '[31]', NULL),
(216, 47, 10, 2, '[40]', NULL),
(217, 47, 28, 0, NULL, NULL),
(218, 47, 31, 0, NULL, NULL),
(219, 47, 34, 8, '[77, 77, 78, 79, 97, 97, 98, 99]', NULL),
(220, 47, 50, 6, NULL, NULL),
(221, 48, 9, 6, '[35, 36, 37]', NULL),
(222, 48, 13, 6, '[7, 8]', NULL),
(223, 48, 14, 1, '[\"Да\"]', NULL),
(224, 48, 26, 8, '[65, 66, 67, 85, 86, 87]', NULL),
(225, 48, 27, 0, NULL, NULL),
(226, 48, 30, 14, '[68, 69, 70, 71, 88, 89, 90, 91]', NULL),
(227, 49, 7, 4, '[28]', NULL),
(228, 49, 8, 9, '[31]', NULL),
(229, 49, 10, 6, '[40, 41, 42]', NULL),
(230, 49, 28, 0, NULL, NULL),
(231, 49, 31, 0, NULL, NULL),
(232, 49, 34, 6, '[76, 78, 79, 96, 98, 99]', NULL),
(233, 49, 50, 8, NULL, NULL),
(234, 50, 2, 3, '[14, 16, 17]', NULL),
(235, 50, 4, 3, '[\"Да\"]', NULL),
(236, 50, 5, 1, '[\"Да\"]', NULL),
(237, 50, 6, 1, '[25]', NULL),
(238, 50, 45, 6, '[100]', NULL),
(239, 50, 46, 0, NULL, NULL),
(240, 51, 3, 4, '[21, 22]', NULL),
(241, 51, 9, 6, '[36, 37, 38]', NULL),
(242, 51, 30, 12, '[68, 69, 70, 88, 89, 90]', NULL),
(243, 51, 31, 0, NULL, NULL),
(244, 51, 33, 0, NULL, NULL),
(245, 52, 10, 4, '[41, 42, 43]', NULL),
(246, 52, 25, 24, '[60, 61, 62, 80, 81, 82]', NULL),
(247, 52, 26, 4, '[66, 67, 86, 87]', NULL),
(248, 52, 27, 0, NULL, NULL),
(249, 52, 32, 1, '[\"Да\"]', NULL),
(250, 52, 33, 0, NULL, NULL),
(251, 53, 7, 2, '[30]', NULL),
(252, 53, 8, 9, '[31]', NULL),
(253, 53, 10, 2, '[40]', NULL),
(254, 53, 28, 0, NULL, NULL),
(255, 53, 31, 0, NULL, NULL),
(256, 53, 34, 8, '[77, 77, 78, 79, 97, 97, 98, 99]', NULL),
(257, 53, 50, 6, NULL, NULL),
(258, 54, 9, 6, '[35, 36, 37]', NULL),
(259, 54, 13, 6, '[7, 8]', NULL),
(260, 54, 14, 1, '[\"Да\"]', NULL),
(261, 54, 26, 8, '[65, 66, 67, 85, 86, 87]', NULL),
(262, 54, 27, 0, NULL, NULL),
(263, 54, 30, 14, '[68, 69, 70, 71, 88, 89, 90, 91]', NULL),
(264, 54, 7, 4, '[28]', NULL),
(265, 54, 8, 9, '[31]', NULL),
(266, 54, 10, 6, '[40, 41, 42]', NULL),
(267, 55, 28, 0, NULL, NULL),
(268, 55, 31, 0, NULL, NULL),
(269, 55, 34, 6, '[76, 78, 79, 96, 98, 99]', NULL),
(270, 55, 50, 8, NULL, NULL),
(271, 56, 2, 3, '[14, 16, 17]', NULL),
(272, 56, 4, 3, '[\"Да\"]', NULL),
(273, 56, 5, 1, '[\"Да\"]', NULL),
(274, 56, 6, 1, '[25]', NULL),
(275, 56, 45, 6, '[100]', NULL),
(276, 56, 46, 0, NULL, NULL),
(277, 57, 3, 4, '[21, 22]', NULL),
(278, 57, 9, 6, '[36, 37, 38]', NULL),
(279, 57, 30, 12, '[68, 69, 70, 88, 89, 90]', NULL),
(280, 57, 31, 0, NULL, NULL),
(281, 57, 33, 0, NULL, NULL),
(282, 58, 10, 4, '[41, 42, 43]', NULL),
(283, 58, 25, 24, '[60, 61, 62, 80, 81, 82]', NULL),
(284, 58, 26, 4, '[66, 67, 86, 87]', NULL),
(285, 58, 27, 0, NULL, NULL),
(286, 58, 32, 1, '[\"Да\"]', NULL),
(287, 58, 33, 0, NULL, NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `AnswerTypes`
--

CREATE TABLE `AnswerTypes` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `AnswerTypes`
--

INSERT INTO `AnswerTypes` (`id`, `name`) VALUES
(1, 'Многие из многих'),
(2, 'Один из многих'),
(3, 'Шкала от 1 до 5'),
(4, 'Шкала от 1 до 10'),
(5, 'Да/Нет'),
(6, 'Свободный ответ');

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

--
-- Дамп данных таблицы `Candidates`
--

INSERT INTO `Candidates` (`id`, `first_name`, `last_name`, `patronimic`, `email`, `phone`, `resume_link`, `status_id`, `created_at`) VALUES
(51, 'Алексей', 'Савичев', 'Евгеньевич', 'asavichev@gmail.com', '+7(962)187-02-00', 'https://hh/savichev_link', 3, '2025-06-08 15:20:24'),
(52, 'Евгения', 'Афанасьева', '', 'aevgen@ya.ru', '+7(945)127-12-12', 'https://hh/afanas_link', 4, '2025-06-08 15:21:47'),
(53, 'Александр', 'Лукин', 'Петрович', 'luka056@mail.ru', '+7(968)167-22-15', 'https://hh/lukin_link', 4, '2025-06-08 15:23:11'),
(54, 'Никита', 'Деньжин', 'Викторович', 'nikitadv@gmail.com', '+7(988)169-04-42', 'https://hh/denzin_link', 4, '2025-06-08 16:12:35'),
(62, 'Елена', 'Романова', 'Игоревна', 'elena.rom@mail.ru', '+7(901)111-00-11', 'https://hh.ru/resume/romanova', 2, '2025-06-10 10:04:33'),
(63, 'Максим', 'Демидов', 'Сергеевич', 'max.dem@gmail.com', '+7(902)222-33-44', 'https://hh.ru/resume/demidov', 2, '2025-06-10 10:04:33'),
(64, 'Инна', 'Зуева', 'Павловна', 'inna.zueva@mail.ru', '+7(903)333-44-55', 'https://hh.ru/resume/zueva', 2, '2025-06-10 10:04:33'),
(65, 'Сергей', 'Калашников', 'Андреевич', 'sergeykal@gmail.com', '+7(904)444-55-66', 'https://hh.ru/resume/kalashnikov', 2, '2025-06-10 10:04:33'),
(66, 'Елена', 'Романова', 'Игоревна', 'elena.rom@mail.ru', '+7(901)111-00-11', 'https://hh.ru/resume/romanova', 2, '2025-06-10 10:10:03'),
(67, 'Максим', 'Демидов', 'Сергеевич', 'max.dem@gmail.com', '+7(902)222-33-44', 'https://hh.ru/resume/demidov', 2, '2025-06-10 10:10:03'),
(68, 'Инна', 'Зуева', 'Павловна', 'inna.zueva@mail.ru', '+7(903)333-44-55', 'https://hh.ru/resume/zueva', 2, '2025-06-10 10:10:03'),
(69, 'Сергей', 'Калашников', 'Андреевич', 'sergeykal@gmail.com', '+7(904)444-55-66', 'https://hh.ru/resume/kalashnikov', 2, '2025-06-10 10:10:03'),
(70, 'Алексей', 'Травин', 'Юрьевич', 'atravin@gmail.com', '+7 (958) 163-05-57', '-', 2, '2025-06-10 14:09:40'),
(71, 'Константин', 'Зимовицкий', '', 'zima@ya.ru', '+7 (962) 120-24-55', 'https:\\\\hh\\zima_link', 2, '2025-06-10 14:11:05'),
(72, 'Анастасия', 'Евлинская', 'Германовна', 'evlinskaya97@mail.ru', '+7 (988) 561-23-45', '', 2, '2025-06-10 14:12:48'),
(73, 'Олег', 'Ковалев', '', 'acerolav@yandex.ru', '+7 (985) 651-36-58', '-', 2, '2025-06-10 14:13:42'),
(74, 'Дмитрий', 'Соколов', 'Петрович', 'dmitry.sokolov@mail.ru', '+7 (790) 033-38-44', 'https://hh/dmitry_sokolov', 2, '2025-06-10 14:49:51'),
(75, 'Всеволод', 'Андрев', 'Андреевич', 'anreee@gmail.com', '+7 (988) 554-11-22', '-', 2, '2025-06-10 14:51:04');

-- --------------------------------------------------------

--
-- Структура таблицы `Categories`
--

CREATE TABLE `Categories` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Categories`
--

INSERT INTO `Categories` (`id`, `name`) VALUES
(1, 'Технические знания'),
(2, 'Коммуникация'),
(3, 'Инструменты'),
(4, 'Практические навыки');

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

--
-- Дамп данных таблицы `Employees`
--

INSERT INTO `Employees` (`id`, `first_name`, `last_name`, `patronimic`, `email`, `phone`, `position_id`, `hire_date`, `fire_date`, `status_id`, `skills`, `organization_id`) VALUES
(1, 'Василиса', 'Бегларян', 'Викторовна', 'abramtsovav@yandex.ru', '+7(988)169-04-42', 15, '2024-09-13', NULL, 6, '{}', 1),
(9, 'Евгения', 'Афанасьева', '', 'aevgen@ya.ru', '+7(945)127-12-12', 4, '2024-03-01', NULL, 1, '{\'Технические знания\': \'10\'}', 1),
(10, 'Александр', 'Лукин', 'Петрович', 'luka056@mail.ru', '+7(968)167-22-15', 3, '2025-01-15', NULL, 1, '{\'Технические знания\': \'8\', \'Коммуникация\': \'\', \'Инструменты\': \'\', \'Практические навыки\': \'\'}', 1),
(11, 'Никита', 'Деньжин', 'Викторович', 'nikitadv@gmail.com', '+7(988)169-04-42', 4, '2025-04-05', NULL, 1, '{\'Технические знания\': \'5\', \'Коммуникация\': \'9\', \'Инструменты\': \'HiHire\', \'Практические навыки\': \'0\'}', 1),
(22, 'Андрей', 'Гончаров', 'Михайлович', 'agoncharov@bt.ru', '+7(999)111-22-33', 1, '2025-04-15', NULL, 1, '{\'Технические знания\': \'5\', \'Коммуникация\': \'9\', \'Инструменты\': \'HiHire\', \'Практические навыки\': \'0\'}', 1),
(23, 'Светлана', 'Орлова', 'Петровна', 'sorlova@bt.ru', '+7(912)222-33-44', 1, '2025-03-10', NULL, 1, '{\'Технические знания\': \'_\', \'Коммуникация\': \'_\', \'Инструменты\': \'_\', \'Практические навыки\': \'_\'}', 1),
(24, 'Кирилл', 'Мельников', 'Дмитриевич', 'kmelnikov@bt.ru', '+7(903)555-66-77', 7, '2025-02-20', NULL, 1, NULL, 1),
(25, 'Алина', 'Васильева', 'Юрьевна', 'avasilieva@bt.ru', '+7(965)777-88-99', 8, '2025-01-05', NULL, 1, NULL, 1),
(26, 'Андрей', 'Гончаров', 'Михайлович', 'agoncharov@bt.ru', '+7(999)111-22-33', 1, '2025-04-15', NULL, 1, '{\'Технические знания\': \'_\', \'Коммуникация\': \'_\', \'Инструменты\': \'_\', \'Практические навыки\': \'_\'}', 1),
(27, 'Светлана', 'Орлова', 'Петровна', 'sorlova@bt.ru', '+7(912)222-33-44', 6, '2025-03-10', NULL, 1, NULL, 1),
(28, 'Кирилл', 'Мельников', 'Дмитриевич', 'kmelnikov@bt.ru', '+7(903)555-66-77', 7, '2025-02-20', NULL, 1, NULL, 1),
(29, 'Алина', 'Васильева', 'Юрьевна', 'avasilieva@bt.ru', '+7(965)777-88-99', 8, '2025-01-05', NULL, 1, NULL, 1);

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

--
-- Дамп данных таблицы `Interviews`
--

INSERT INTO `Interviews` (`id`, `questionnaire_id`, `interviewer_id`, `candidate_id`, `created_at`, `status_id`) VALUES
(47, 76, 7, 70, '2025-05-11 14:09:40', 2),
(48, 71, 7, 71, '2025-05-10 14:11:05', 2),
(49, 76, 7, 72, '2025-05-10 14:12:48', 2),
(50, 69, 7, 73, '2025-03-10 14:13:42', 2),
(51, 74, 6, 74, '2025-05-20 14:49:51', 2),
(52, 72, 6, 75, '2025-06-10 14:51:04', 2),
(53, 76, 7, 70, '2025-05-11 14:09:40', 2),
(54, 71, 7, 71, '2025-05-10 14:11:05', 2),
(55, 76, 7, 72, '2025-05-10 14:12:48', 2),
(56, 69, 7, 73, '2025-03-10 14:13:42', 2),
(57, 74, 6, 74, '2025-05-20 14:49:51', 2),
(58, 72, 6, 75, '2025-06-10 14:51:04', 2);

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

--
-- Дамп данных таблицы `Organizations`
--

INSERT INTO `Organizations` (`id`, `name`, `status_id`, `description`, `created_at`) VALUES
(1, 'ООО «Большая Тройка»', 1, '', '2025-05-25 14:26:04');

-- --------------------------------------------------------

--
-- Структура таблицы `Positions`
--

CREATE TABLE `Positions` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Positions`
--

INSERT INTO `Positions` (`id`, `name`) VALUES
(1, 'Аналитик'),
(2, 'Бэк-разработчик'),
(3, 'Фронт-разработчик'),
(4, 'HR-специалист'),
(5, 'DevOps-инженер'),
(6, 'QA-инженер'),
(7, 'Data Scientist'),
(8, 'Менеджер проектов'),
(9, 'DevOps-инженер'),
(10, 'QA-инженер'),
(11, 'Data Scientist'),
(12, 'Менеджер проектов'),
(13, 'Бизнес-аналитик'),
(14, 'Логист'),
(15, 'HR-Директор'),
(16, 'Тестировщик');

-- --------------------------------------------------------

--
-- Структура таблицы `QuestionnaireQuestions`
--

CREATE TABLE `QuestionnaireQuestions` (
  `questionnaire_id` int NOT NULL,
  `question_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `QuestionnaireQuestions`
--

INSERT INTO `QuestionnaireQuestions` (`questionnaire_id`, `question_id`) VALUES
(69, 2),
(74, 3),
(69, 4),
(75, 4),
(69, 5),
(69, 6),
(70, 7),
(76, 7),
(70, 8),
(76, 8),
(71, 9),
(74, 9),
(72, 10),
(76, 10),
(70, 11),
(70, 12),
(71, 13),
(71, 14),
(72, 25),
(71, 26),
(72, 26),
(71, 27),
(72, 27),
(76, 28),
(75, 29),
(71, 30),
(74, 30),
(74, 31),
(76, 31),
(70, 32),
(72, 32),
(75, 32),
(72, 33),
(74, 33),
(75, 33),
(76, 34),
(69, 45),
(69, 46),
(75, 46),
(73, 47),
(75, 47),
(73, 48),
(73, 49),
(75, 49),
(73, 50),
(76, 50),
(73, 51);

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

--
-- Дамп данных таблицы `Questionnaires`
--

INSERT INTO `Questionnaires` (`id`, `position_id`, `title`, `description`, `created_by`, `is_public`, `created_at`) VALUES
(69, 1, 'Аналитик', '', 2, 1, '2025-06-10 13:40:22'),
(70, 3, 'Фронт-разработчик', '', 2, 1, '2025-06-10 13:46:39'),
(71, 2, 'Бэк-разработчик', '', 2, 1, '2025-06-10 13:47:43'),
(72, 5, 'DevOps-инженер', '', 2, 1, '2025-06-10 13:48:41'),
(73, 4, 'шаблон HR Евгения', '', 6, 0, '2025-06-10 13:57:05'),
(74, 7, 'Data Scientist Евгения', '', 6, 0, '2025-06-10 13:58:15'),
(75, 8, 'Менеджер проектов Никита', '', 7, 0, '2025-06-10 14:07:02'),
(76, 16, 'Тестировщик Никита', '', 7, 0, '2025-06-10 14:08:10');

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

--
-- Дамп данных таблицы `QuestionOptions`
--

INSERT INTO `QuestionOptions` (`id`, `question_id`, `text`, `score`) VALUES
(1, 12, 'React', 5),
(2, 12, 'Vue', 4),
(3, 12, 'Angular', 3),
(4, 12, 'Svelte', 2),
(5, 12, 'Без фреймворков', 1),
(6, 13, 'Webpack', 3),
(7, 13, 'Vite', 4),
(8, 13, 'Parcel', 2),
(9, 13, 'Gulp', 1),
(10, 1, 'BPMN', 3),
(11, 1, 'UML Use Case', 2),
(12, 1, 'ER-диаграмма', 1),
(13, 1, 'Не использую диаграммы', 0),
(14, 2, 'Confluence', 1),
(15, 2, 'Figma', 1),
(16, 2, 'Excel', 1),
(17, 2, 'Word', 1),
(18, 2, 'Jira', 1),
(19, 3, 'Интервью', 1),
(20, 3, 'Наблюдение', 1),
(21, 3, 'Анализ документации', 1),
(22, 3, 'Прототипирование', 1),
(23, 6, 'BRD (бизнес-требования)', 3),
(24, 6, 'ТЗ (техническое задание)', 2),
(25, 6, 'Пользовательские сценарии', 1),
(26, 6, 'Диаграммы', 0),
(27, 7, 'REST', 3),
(28, 7, 'GraphQL', 2),
(29, 7, 'gRPC', 2),
(30, 7, 'SOAP', 1),
(31, 8, '80–100%', 3),
(32, 8, '50–80%', 2),
(33, 8, '20–50%', 1),
(34, 8, '0–20%', 0),
(35, 9, 'PostgreSQL', 1),
(36, 9, 'Redis', 1),
(37, 9, 'Kafka', 1),
(38, 9, 'RabbitMQ', 1),
(39, 9, 'Docker', 1),
(40, 10, 'Microservices', 1),
(41, 10, 'Clean Architecture', 1),
(42, 10, 'MVC', 1),
(43, 10, 'Monolith', 0),
(60, 25, 'Blue-Green Deployment', 2),
(61, 25, 'Canary Release', 2),
(62, 25, 'Rolling Update', 2),
(63, 25, 'Не знаю', 0),
(64, 26, 'Jenkins', 2),
(65, 26, 'GitLab CI', 2),
(66, 26, 'TeamCity', 1),
(67, 26, 'GitHub Actions', 1),
(68, 30, 'scikit-learn', 2),
(69, 30, 'TensorFlow', 2),
(70, 30, 'PyTorch', 2),
(71, 30, 'XGBoost', 1),
(72, 31, 'Линейная', 1),
(73, 31, 'Логистическая', 1),
(74, 31, 'Полиномиальная', 1),
(75, 31, 'Не использую', 0),
(76, 34, 'Модульное', 1),
(77, 34, 'Интеграционное', 1),
(78, 34, 'Нагрузочное', 1),
(79, 34, 'UI-тестирование', 1),
(80, 25, 'Blue-Green Deployment', 2),
(81, 25, 'Canary Release', 2),
(82, 25, 'Rolling Update', 2),
(83, 25, 'Не знаю', 0),
(84, 26, 'Jenkins', 2),
(85, 26, 'GitLab CI', 2),
(86, 26, 'TeamCity', 1),
(87, 26, 'GitHub Actions', 1),
(88, 30, 'scikit-learn', 2),
(89, 30, 'TensorFlow', 2),
(90, 30, 'PyTorch', 2),
(91, 30, 'XGBoost', 1),
(92, 31, 'Линейная', 1),
(93, 31, 'Логистическая', 1),
(94, 31, 'Полиномиальная', 1),
(95, 31, 'Не использую', 0),
(96, 34, 'Модульное', 1),
(97, 34, 'Интеграционное', 1),
(98, 34, 'Нагрузочное', 1),
(99, 34, 'UI-тестирование', 1),
(100, 45, 'WHERE фильтрует строки до группировки, HAVING — после', 2),
(101, 45, 'HAVING работает только с агрегатными функциями', 0),
(102, 45, 'WHERE нельзя использовать с GROUP BY', 0),
(103, 48, 'Платформы для обучения сотрудников', 2),
(104, 48, 'Системы мотивации и поощрений', 1),
(105, 48, 'Аналитика HR-данных', 2),
(106, 48, 'Корпоративные соцсети', 1),
(107, 49, 'Конкурентная зарплата', 1),
(108, 49, 'Возможности карьерного роста', 1),
(109, 49, 'Обучение и развитие', 1);

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

--
-- Дамп данных таблицы `Questions`
--

INSERT INTO `Questions` (`id`, `text`, `weight`, `answer_type_id`, `category_id`) VALUES
(1, 'Какой тип диаграммы вы чаще используете при моделировании бизнес-процессов?', 1, 2, 1),
(2, 'Какие инструменты вы используете для описания требований?', 1, 1, 3),
(3, 'Какие методы анализа требований вы применяете?', 2, 1, 1),
(4, 'Вы проводили демонстрации прототипов заказчику?', 3, 5, 2),
(5, 'Требования менялись после согласования?', 1, 5, 2),
(6, 'Какой документ вы создаёте в первую очередь?', 1, 2, 4),
(7, 'Какой из форматов API вы используете чаще всего?', 2, 2, 3),
(8, 'Какой уровень покрытия тестами вы считаете достаточным?', 3, 2, 4),
(9, 'Какие технологии вы чаще используете в проектах?', 2, 1, 3),
(10, 'С какими архитектурами вы работали?', 2, 1, 3),
(11, 'Насколько уверенно вы работаете с JavaScript без фреймворков?', 2, 3, 1),
(12, 'Какой фреймворк вы используете чаще всего?', 1, 2, 3),
(13, 'Какие инструменты вы используете для сборки проекта?', 1, 1, 3),
(14, 'Приходилось ли вам самостоятельно внедрять SSR/SSG?', 1, 5, 4),
(25, 'Какой подход вы используете для деплоя?', 2, 1, 3),
(26, 'Какие инструменты CI/CD вы используете?', 1, 1, 3),
(27, 'Как вы проверяете качество кода?', 2, 1, 4),
(28, 'Что такое тест-пирамида?', 1, 6, 1),
(29, 'Как вы управляете задачами в команде?', 2, 1, 2),
(30, 'С какими ML-библиотеками вы работали?', 1, 1, 1),
(31, 'Какой тип регрессии вы чаще используете?', 1, 2, 1),
(32, 'Использовали ли вы Scrum?', 1, 5, 2),
(33, 'Какие метрики вы отслеживаете в проектах?', 1, 6, 4),
(34, 'С какими видами тестирования вы знакомы?', 1, 1, 4),
(45, 'Какая разница между WHERE и HAVING?', 3, 1, 1),
(46, 'Как объяснить сложный анализ нетехническому заказчику?', 2, 6, 2),
(47, 'Использовали ли вы методы активного слушания в своей работе?', 1, 5, 4),
(48, 'Какие из перечисленных инструментов вы использовали в своей работе?', 3, 1, 3),
(49, 'Какой из перечисленных факторов вы считаете наиболее важным для удержания сотрудников?', 3, 2, 1),
(50, 'Насколько для вас важна работа в команде?', 2, 3, 2),
(51, 'Оцените вашу способность разрешать конфликты на рабочем месте', 2, 4, 2);

-- --------------------------------------------------------

--
-- Структура таблицы `Roles`
--

CREATE TABLE `Roles` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Roles`
--

INSERT INTO `Roles` (`id`, `name`) VALUES
(1, 'HR-Director'),
(2, 'HR-Manager');

-- --------------------------------------------------------

--
-- Структура таблицы `Statuses`
--

CREATE TABLE `Statuses` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `Statuses`
--

INSERT INTO `Statuses` (`id`, `name`, `type`) VALUES
(1, 'Работает', 'empl'),
(2, 'Новый', 'cand'),
(3, 'Отказ', 'cand'),
(4, 'Принят', 'cand'),
(5, 'Уволен', 'empl'),
(6, 'В отпуске', 'empl'),
(7, 'Ожидание ответа', 'cand'),
(8, 'Приглашение', 'email'),
(9, 'Отказ', 'email'),
(10, 'На испытательном сроке', 'empl');

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
-- Дамп данных таблицы `Users`
--

INSERT INTO `Users` (`id`, `login`, `password_hash`, `salt`, `work_email_password`, `employee_id`, `last_entry`, `role_id`, `is_active`, `avatar`) VALUES
(2, 'qw', 'c59c430761f4e84efe9e144ef691f7ff2f3bb5121681041d0b14a0796b075220', '6cbe352d97bfa495e79ae780d26ce913', 'bbmapiqdxtnzhvjf', 1, '2025-06-09 21:38:19', 1, 1, 0x524946469e230000574542505650382092230000701c019d012a200320033e9148a14c25a4a3222314e848b01209676ee9de6856afbf4bbb3f2dff73fc07eddf8f165ff2dfdf7f74fa0dbaa7ebdfab7e307f91dd6c867d98f957fb7eb8ffdafa9cfd71ff97dc23f5f7a557991fdd0fdbaf788fcb1f7e1fdfffd8fb027f33ea59f411fdc5f4eff67ffebdff1b290be7bfde7fe0faaff9cfefde43eae5bc5d1273dbd8efedbe21192fd8be00bbca7f0fce2fe7f5b46801fc83d24ffe4f2f1fb3ef95fde20e003cb58c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c465b4f67d606f2011075a8e49c7f4beca6f00419fe0bab35a9490390eedb48bc78289a48c788d2463c469231e234918f0a4009bfffa6633bf823383e43c71a345982c47c25c5cc12aa9226234918f11a48c788d2463c469231413be32662fdcfcb45e7788d2463df33bb47533e932a74289a48c788d2463c469231e2214026699371b0390baaf356b18f10fc193e61898543b7b4f2d631e234918f11a48c785200b1097ce963c468e70f1cd4f61944696fd2b7de194e384e4abb62901aad631e234918f11a48c75b807a503687dd2b7b68ba4cafffdf996b3920a53748e9e2d7cfd06478b92f2d639da9940015dcb4e556b18f11a48c788d2462866341093677c7d8996208df8ad345a4ffc24a0aaf6ef79e2eeb3963cde9860933ded0adefe579ab58c788d23a37c4a8d07c9065568e4fe7c176f540a2691d7350fc6eb6af7d89a371c15821a63ccffa56f7f2bcd5ac63c290052486c8ea463aa9394f2f8ab1bcaf354e860a9aa5a54add236a328a550f50a269231e234918a16f3930fc8b850a06775911745bbe989013ea6386f39372465fff6ebadebb2b0a0977eefff5e6b1160cd695bf1fe95bdfcaf356b155e5e3e6919476314dff97dcb2857af01e8b54f731ae806b91503ea644628287ffe06553350af547a0fe579285aba7c794289a48c788d24551bcbb2343ac248c54f16be95da4d59c254da24125f709b1f74464aeaaefa0d6b164152ddbf6266163845d5dd75b50a269231e2346f103c1dcc4d2455f0a017a0ee3f1c2889f63ad1e004b305551bd17cf67d18b97ffe8151ded76df96f45971752b75316de4bf5fe95bdfcaf356aec44234370c92b7bee8221f3872d9d5134a99515bcc544b1e0160598647392e47a130d15a258798ba305361bfe501a3cb58aac81b6d6f87243ec4d2463c264f2ee58c7888331d8afd3aed8382a4976a9965f24a8deb0921b44406a32bf257a5bb405837f15a6dff96b18a56344e6cda85134918f11971f9afcb57dce169d23c343efc18fcc3fa774e94ca9a8647c200c2a1b3a83f1f0b7d448101a3cb58aa7f11956b356b18f11a48c7584b3fbfca69636b76f92c3c2c1e8ee47eae7d9396cabaea968bf17d9995ef48a671d3b033b8ee6c643ac6f5301caf421bc25d0079106af74b3cdcb03165673c319b86ceac3c5caa0745ee97ed90000a0d1bfb9c6aa654c648ede0b09e733ec542a233720ad0f9fca5af9d4c38ff4adefe579ab476185b828254a822c7f88f562a91b10cc8acc8570e8c0423a5e473ccc2865a49daf8138001f5f6d0a0efb29d47438e4fe952afa81c973214ad7abdea7c34c76594ca42a4662b085973a15412f978379e9b129e498063f1aec839b577b74ddca3d0a071a62ded604231e132fb51f05134918f11a48aac5df30a4ef2400cf06f42213ac76513e5af8d11d464695da01c7df261575753d2a31a6e1c9c0f4de8a0a42b7b6ce523d1402b7bf95e6ad631d5f36bce5bd42899654f995f1e7f9f1b1110cd8c77c14435a3ff09fa85bcedc8700fb1346eb0ab8186b18f11a48c788cb7352d6939e851346ebbf00b4a9f933703fc7688f7eab6652a82275f256c55a1b01da64bdebd03334a0d6f96b7f4add6417a036b4d79ab58c788d246515bfc0f5796b18eace36e34a99cfc8594122fd482d007e419785b53ccc8c901216e0b55ac629b1277def2144d2463c469231d54231ca22cd5a45010df888f584152997139b7e968e5a3c5abc76b89696bbd504b563d42f3c0a5a4583ec098cb83f9adfd2b7bf95e6ad6314bbc7f263ca6a1e5e54974713b5d6b4894994169ee5d04688018b33cbdd394e21e268b07467a5a84daf278d8b2c1cb2e07090ebc94eb9fb8aa95695bdfcaf356b18f0921e59c569c6c28f7637d2ecc098a5fff52157f1bea6bfb02fce5eed291ffc635abfdcfad0f9b247ad534b83ad71d452346a803174c01671e5ac63c469231e2349b4584b580082ba201634aa0cd6491f559691ac47f7476b4e1024f9a2c138fe25c285134918f11a48c7887d8bc63cfcaedc851eb84c2d83ac90fb134918cd89496ba529c94afdeb816045ac63c469231e234918f10ffcb6a271fa79e508057d17ea98a95bdfcaf3568eefc12c411c9475e42bfbbf95e6ad631e234918f1196e8b3ffd0a78fa0ad3fed81f6269231e21f5137f6c8406ed507cc6fabf11a48c788d2463c469231e2346ce14171cb79524f3e37bf95e6ad1c7cd83cd9a6262856f7f2bcd5ac63c469231e2348eb1015fa77a87a214447a43b089a478d2efff05bfe1bfc2f02f356b18f11a48c788d2463c469231e292d66de8bff3a93ef6a0613384af134086e5b8e5bc422350b1a53570a64528a84dfe92bbf95e6ad631e234918f11a48c788d2463c4698ef3eaf01bf7ab58c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11a48c788d2463c469231e234918f11960000feff8208000000000000000000000000000000000000000000000002aebe9c293685eeb369fb4e4bd13962650877357b23cc428b24ed2bceeafa87414295d81f607a70de692796e2304e45e8ba358ef234b2bcb19fcacf6f58531902b43e327b2920fc556fe884eb72ae845c8f47b47a780115743ba29a7764ef3fbca5f1bc4e9febda9c227bab87afb9618be2e3602dd4e516b2e9cee296f257c5bf96a9e08f992b22eeaa80567a664fd94669464e0664d61f3f40ab480ef0aceda91403da809948b4da4abf17b57ac568d3276618289acdcd1cf36767532a182bafe6b60fb83c627b539ddc8d790d73a58b70836937cf4ec511369cea5841a3998816470f70e0c1fd30a978e4a000437d4da6f4e5bde3679f509eafa1da3fd943512bacbce0d308dd3ec7a6d32d7167e3ac8b4e13ec7d1097d0e05051e5c9f9765eea8b0dfa38b76084a8d82ad82c4230ed031dcfb25a804664bdb4c85ce98eb8261a0034fcd6067d30baf3780c424780eb0000548678547a45b8d2d1f052b41c678bbfa66f9de955057579bd1246aa91801d4d21b723f3c5b08f0a9a768d0f7a3d21926bf1d39e42e9b735d3c27f3424acdd8b56ceda47d1ea5c2a6c3f64dd349002270a61221de457c31b483e26fdb9e4361637ef4976eff4df4c5657b0b3bdc8b1601ab754db35911290105a41cc94195791cafeb15afa84dce4ad4a83287a23747a8e9a8c7213ba24a5f7661e012f9c3bfc01603aefaf0003971d800c2f5357c6e6b5ae08cb33ae121310238c285bf69739cc054b1a5f30aa246ad46f590ec5b25d30a578268fa7df9effbce68faead636ed9000269a7ce845e769324c8c8fd8722244e5d35e93730725dc23c9944cb3bda59c3c9e2c88032880449c00b9f85d150910ca7e39701300662213710860b918a40beb96f4cdf9f2c8222a4aa4037800b6c54b61611a62caef3e5e6092ba2dcc6d58002d61ba6b41d800b468dea1a8e6c5027e1233b166bdf561811002b50020f7f179f14f7c600dadcfbb8a4d2802604e1f25815c974310067a8c8fdef3e1931ca89e7a03461a0bd2a633b7ff898c89213b6503d53a1401ecca00b2ca843fdba9d91fe917ddd5800890335d94edd5f64909165e18de80848f5e5b15b98ca2f1f6b83dc7e8a0f3347cf706aa16a1581ff9c5c1601e991e7222bf22de3d299ef883def78612e4cb271a05371e1cce3c180877b35245e7391a24cb7db16ed1939a6b2f8753ae26d80272499d53eed4881a048f80c16503d53c023f3d6cb337ef23ca3819d8e2c53cbef32d629417fc421d7277d33d418c7457aa8285a01ac548af2b3692370e348917ab750478d5f7250b8ea61c51748dac1293f1178c127f56544cb96b81324c9070d922c523036f341af90840fd2de03e3775145daf824b849ee3ab999eb04e3fa92b0cbf954429b0a137706fb79929d6ce237fc36fda62d668b3f6d6a350c331d77b323f7c8dd8c4d816f2d1f5fface50877ef60f5152dc6c6d1484f5f49ba471f7e322469e26434cbc1a63fa1851c4a79aa2ed5904b7f2c2260ac66d87f08ccfb82d55ba51b4b8f11990f8d3d02cfdb25f75baab9f2625a3cde40b61c8519aa4da8e92f38faafc280c06137ac310ef9688bb3888705547154bf2503788ccd1472f7d8cf7950ff275153c2bb43407d551953a7c00765a4ebefe7b2302861384d800638032a8d1c56738913a568b9eea19f3b48fe30677bcfdb2ff55eece08a55c283d2b7326407ff6234ae2ac1f5b44fed7bdc1ca8e5e943941d54a758ecf816e20059289cef960fa73b0ecde650f1e460e01defc5d1defc0b5859bc30e93f068e3e4c8f68511485d81f600910cde026953e4f138a8c97bce71ad284ba168db17649fca9c66073d6b6103c38470f1e2f29769e41948f8a5c923cdea8a00f5f7d7dcaa70aa9d7d176b58c8b787d3606c084c10c26fca3298891dea11cea22a46a241bbca966caac9ece078972dccdca9654e9e599ad5b2304fdf2571795700f231516f798c34b2ebc7b7c9447c9d0166db851dfafd1ef2a9287f2363ccb196b564f62ac3106cc998115381b71a484af5b137344db2cc70f5ad20cd034f590a86f2dc039602e0fed8128c0a74c8c29fd1c63c37428ffe1b108f7141a49bcd6237af32bcff869145178dcefc0071afdf6e779090d8057c5003b5887958b6f142a41e00586d2885de9d32da87205e73bea8891459ef747ed97c1ed74810e3c4e0647695616e4042e45b3fe79a098c101a3c977b60692c94e3ac26a4a111ff586e7d5f56ca7c5eacd6eeadeeef734844c266871afb20a516589318dee251d4231fe5ebd0a379baf3bce331f589a4ee98d0140957b759cb194b9ed6f72e42ce7865ff788d20c83f2b1c4e0d4d466a44d7d18ed2091fcb38e19b2654ef30685f67fc3f8d081af921b07c4eed7e803efcd4ac2beb1e65bf7a45c73505cb903cc02cbca52d6c15ebc5c662df4dec4d129639b5cb2125d5ad856681b0c63d648482bc8bd867ba6b0062ad740aae407d4e92e52713eda21bddee393d76225fcf4687caeff1adecc1eba03f00f92b1e33105af5371c6dc6d1bd0dbefa23f0da9db1d6b11b06c8829ec1b68c77d0209f2f6667d1c4d2fd73889313aca3a241e1cca3a949ce0d6568ba0da07248468892afa1c216a0007481b71c9495d87361ec8b30fdbacc06b95d90a126329a2f04e7d9ca6caf5b672eaef937a6c77d42a305fcca3c9d39ee623ee882cdd691ebce977e3af9d226c47c5d8e515c34b35f5fd93590e7880d342577346e1fe42356a5ecbde1d6078394dc5a585a352ca6cb74c41339aa394d4fa2535e48e1ad5213b2a8ca6089ab68bf47419d51983aeaaa36b12b4e9fb3ab8fa3ece15fd81125584c827329da010cc7499e533769ce395e614fe0e6dad46d331bc7045e0fd22a2d848285e6bc6e6ab1c4c4368a607b4081f2d0446dd2ab01493d7aa970603fb9eed36f1cd3368fdba70e4b1d9e000c79a15f27da5da2c89679b435b68219733ad89fb59e305276f9de2e2120c806e7252374371f275d98c0a622af974138836288ac19cf9c291e98dbaf1c5dae7746dd4360acd7bf5d6027e53b35ed59a2f7a373bbdb43f252cb4c6d6d98a5dd7071f4e2dedc51d70d0f25b6b03899d47fb00e3b0b9b26f53d17f038055e25621d9551661de502f4e200a331232814ea5b93514f551d1abcf7e9f3552e9cb4df678a71d05f2fc2bfb05943ed88c8d99772d149444d49e5a0dd58f61cca0b0a63f28d41875d111e9716e91bdf36aecaccb5336293a89ee79f5640060396d5f940ec315e88548e19454676875f85d536aee9f267293c6c1dfd26d0b88386e5e8cd0127a0486be46c2f0f53314cdb21ada821b1c5cbca9b9f4a7b4b857ffbc809735554ca6f44411175006c638bd8e69176dbbd426a4fcf752d8e84605e42132cd9e0ad5da8370e32fe7454720abd8e892acd9ce037f530df73f3acef85f6d744f8c1b8ab4ee2b1204972aa4bb782487e5853120449c7d359a9176787803003f6b81dd20d8ee0ecd166cfa1f8e071e76c0194765320115635032f1747344a42a2fb191c44613437fa359a1b1194fdb642d26a8936f2ec79e69ca8bba9382025c591ab92c364970309a5a72dbe164c7293ae4bbc32a219e9babb4c86fbf5c92a3e37b7af9912701731cec1519719247ceef353bc00648887ea1c58481cdb548f92bd1e9abe986a7765ef4ee1d3da732b524554aa01808ac16d24fdb8a4e96b2a41bd139081235bc1046139c48c9cb43d2cb5487951071391b9e5ff2e7e575a60a7f4999498fc67b76c683da9406733e95eda97205b90dec9af4ab8d506cbb75265d7ce176b3781ea79e1cfcbd71b840052fa0cfc8c10d05b06a4e4f82f3ac6be15fcd79a46233acabaf230d17775565879a76796435c188d8c1a0a671c1ab5b06a32e8fed5023e524099a1cf6acf7570c496d7fd07b58d5deb3f905a46e6d346073310042cd72f00ce18210343820748614031d1d812711a8b7e6cab0b43bd03cb1feca4e6ccb0e6ee1da1322bfe718b6cde9a587ce26716a969627a53f2fae7e4f69e749b1e8d6f25a37775411b8943251a1a7a44676353b577aebb2ca343c9ac7ca69b197c2ba4ec088d64c549862ceccb6d2993c5a228bbed0404c138d778d1bcb0bbd09d081876101c9abfa753de277415d5b68a8558cf62eb703859174400394ec777c49bfaa6e312c5840f5201fd437900bf3c44c16c565d1530afdd773463b56bef390ed8f9256ff0248b81945fd6cc5f05ee632a168e098aa813ca9bcbc16bdcdb1b64238b407d39b02252d02b07390e87189ae813dc08e2f4ec477143d2f22b37c898b3ec281b975be5620dc29d27426a924c78589c34041ec9372e3cb5e05f53ff22d2d4091418b46c8a3ecb4833f1679422304922e2b9f532649eac487ef97bc0001ad2c18ac64f865be1eda5ece00dbcb077e6e15cb2d95966a78e0b7ed5436e999fe87ec4267dc51062325b36fc1c21150574656669da3ebe19799210f4e5c72aedc1198da50a1aacb40f6a8cd0fb1750ebf1e4725c66e22d024269e1fbc65b0217244e734389b0789cbd65faf1938fd96abf34f024301840666d09e069923062622063a5316ec318e6a9656f0e50c431ce6735f712d0e2fe966f0a651705237d8179adfa0db73aba4705d1befc9a4d04efc580ea133296f269805fb7ed26f014f3ac639a59f2fc188ca1c455a6e9bea2323a2c9051b6af1c0abc634b36f5508a28f2a62ddc49560dbab52720af895dcee9a62a5a10756f4ba060888efd65a5b348d4e5ffecd46178016c12009d483adf2b6780d64393066c866a6af6a13e4378fd87a7f26afdc9c6b60ffcec48db00100072125d81b3b3d9216ec8481a7a2dae3d25811bda5432e2dd2df793ca5b01aa6c700eb5e44e2f65d51a45cf72043b3fc48390a336e05accbcf548fe2f5d6a0f01f620d95477f5f1cbedf61af8486a7b4a9baa5c996e0808cdeb1b9ade65639d7a28fc44d2658d45e17b399b2ca05c9dde324f9c06578e3c69d7dec936ee7a151ebf9ba2d3e9ef64216deff91f2eeea53ae37a1f2be229e2ef8808b85f50f7502ab053e17d04c23e0ca4db77ce16fe078e49d1cc7cdbc7bb5a07fa7e28ae1d106e452b94c4c289baa741d76cc68e55da3d5fe7fd6a8de2d08a440a09881cf4b0ec4231ad9845ef76d01178ee0975264df14434b6cc74db8b801ac2467ea5a70978dcf4fe52ea65f7b1dca91df6a64c8f27428afa7e86c18c073a8d39481a30c16b4fd2ebd43574a5cb25939ca373206f26d3109072cc28374e52af2cda67a21e3e7fa0a1957290c9abaeef7a0c258f929b78e9d0da5b8d0f12d0d7e34402f7343bd52f746df91b273d79d76e3ce4980e1d319aaeb25ebe63d0751c91a3b005b8fe2431b7485fef2beb7681eadad50f8c2b24415bfc5717f2c48dee216ea8c6bcf852d88c5d599b81c77751c232a2c0ea05b7d82d11d7eae88b31d11f4f7a4cb6734465b674b4b22095c8186b1145922cb092a91cba235e3c6a6417e3fef96be055163b8af76b6806cf30fc1c18a9e596d6fec3b782ed97aa1c3befc3e2db11efd74afadb74c0944a16959ad968e088065d07e7b46850e555753bd4951774a8174f514cb0296361498c8153c1c72182f39bfcc6dff4f8d7a6378865b31ba082073aaa7d14457227e683eeae2e4bf5a594b0559ba9dc5106a6162fb144a7aabdfdac00221e43227c22362378ddd426c104b8dbce01447a6917edd9c1f5ef52ead488bfc8b0863d91fbf1f85e508a8522ac4a532c64408ba26dea96fd9aa2229c0c775986c7e554594e69bb572d6e7328c837eff1db7810ffd26215266f4445d066de149ee20366e790a33055855990a2568c60a5d6e79010e66cbe25dcb80953bb32e00611f5bd3844cc1e0951ba639793df4896f194b494100fcd4e29b5265598dc8708d6ba36ed1c9f8e60bbe7984eda8d9f281976de8616f0cd2842df2d73ac4a17d33ee6647d448f5cb2000d32c885feba65264d25868826d24f15601a1fc7766548238a1d75069af3f6b8eb06271998d0992064f65f2cf3e8502d2d8553a433ac8e4db7e463381a3f8828576626298117ffe1ddea421753c4a7f58ab199ac8184b6183cf8b6cfe0c427dc9783f0559b42886a7afe38484ccb47c5d65cdd9f6de64a1817f43ad1a4e88bb26c761ea287d0b57999bf77e67a7f7aac9e05a2e78b08d253207b690b3f300f7a8f31fbea90eb9892fb7a044132b6ed9cb2c166ef0528992acca8976c8a1dc9d2ee88c751c299e429ae89b2ffa7fe0c66785282b183eb6cb71c130f71430a5efaeb7691648b686f75c42fb3169aab65a6e73b99f11f1507b9f8c8d146cdbaa38b4dbfa2c23db7508c80adb436ee827ffc246c1c199bfd25e312c38e88f3638ae3be5d78fe98e2b4a7b582049a23ade4ce4c10e654cc63b73b2c08dde7cb2ef03396dffa9b76c68e3d3e882c8a5af762ade38e6c45e25125ce6f7381f7cc9b5f23c36dbb87639ed3948a32793a52282ea8ae1c3c58ce26385ec0cf90517bc1ae6b4446d564dbf22102e66a86e7b779b67037a80e5dc30074b38ae7c4acfe96e4638227ed6859ace4a0e03f7ba3918795482929d34a1b7fda726c9d4251969b243c7352674b4cf62d933abafd98c0f3d8208c85316ea636643067a947ac872407e4f769b9f7fdbb7af5dbbfcadb709c1e56dd7e33b2c539ae8d36e57b083005c93fc95fdacbcd17b728d18e65298d63ec8dd211065b3dbbe7547525e7f91954cc53f35332a872ef549961d51eacfbd9c5c033153e191bb8ff5f1c10d7dc77667980fc7b6c1adee90dc864e5de2d09d11a56a9cca344486b2ffea4255ed54d950b145780a8289a09d47a97edf2f89dfa56efdd022bda0967e2e054d0e47c0d083e76a8a9860242f8f42d28e5fe61014ed96aab8bee0f05106e29edda18377a706d98a6215a0c52748782365cbbc05a8b50a5cffd683c90e92df3aeaef5c1b43b85683a0468d017b92f7213703928bcf52886d4a6fafac36b552613a5fd01c2999c0dfff5e735f4113b8a88e6c359cdfab69886f870644898796f684869fc8e4da8b3816f1c3edeebaeeddbe726687b5db2714fe7b66396265a695356e76e36c07189ef03846a275339a11a9011a78c384edb69845c75f568df5e84dea74be84984c217388e2926a621f172ed058dba3d4ea52b65d8d2e0abeaa8ca246df7c82e3df2730000477d19b313496d17752fedcd5eb5e04b663424ef8f07408179ce007312e9bfd03beee6d0d805ad71a54c6d079de8e907929339b3d61a29bc05e98da906d7ed37ac42bfeb10fbace6e34934a936d33015fdd93529216c0b6166052dc456242ae0fddfacf41f2df4e862ef51453fdbd55a06e43e02111e5a1d97b66c8c41b2a80d86e0618406b209a0c265525ae703311ba35972217379bcac35b5778b779098950cba5e6235190ebb97cb9171dab839611500bb2fa51b193a45bec78b3d78c8c228cc4176c7b0d96e04008c4767491feed38a026346e92e5ed989fc1952ed74346f3bba3c4a611147a8f40179ddeed14d365941662c6fdf60548f65f879a8cd92b698995770172ade70c639477357c5437c8f126b6e2ffa33ce6bb7c4ecefdd673789082cae72d7f83d3590413b8d48f076e335a9d4edb16c1287bbaaee16f2192c1fa6a84023a5eaad54ec5da44bd1f7a206d694d4b3b3a7fcd4344023c65a473a407f08f2dfbd69b7532d8d967f4a0b50a9d0a23b74071fcf5b98923344170d92dbd1fe21a457308924474db7bb17db66f1843e4464741564d261629adc04dcefa82cabbd6e216d2ae868b9f69840d3d7ff9f7ce1f2201e352231d6b32e44079b9f8d4372f29d44def063be4bda001dcad1f783961c9d32df7b68edbbd6d2b99dd1c1c6863ee45340ccbf841a1aac63cefb629461177c1f32e3aac067d6d96c1de36c3acb19c735507704673aa3cd85380b23c7eb3bf6e160fbef258e9b280c039a095d0eefc1ee18922953547cd404dffbccecadcb2a279b1a0d5aeccfd7b5b7ff692e89d5b2317bec49df800fe90541beddbf528f5805fad3f0c53c6e323e0ae74fc3894875cba01b1dbb28cb83e9610bbeb3a6312c5d79643089f9d0b9215da5c89190520d52fc8959231c958209002297ea814a7b15c9860c5a75c7fb01298efa227c163bcc3a2de2ab8b337b41882cee5dd9f3ae8c22edab39207d7f2db975785d8d193c4783522e724e8ac0dbab5799e800b9a89fe7a08de3bc42d845f29c6f03a0e8a88b486dafd1fdeb8d667dcddc97efadf863b971adfdb9b7969a17f65fd95e3df69ab0083d04d0257a53e097d6c699574be5de07ec000013297fabba25e51e78d84a50bdc09742ea3c527a65c2ab72efbe5fc3e96548dfaab6bf8316fe98c065ce6fb7a295e527e2bfcfd698a2775f94957dce404a4cb7b6008d0979f2ca2aa4b48d66215fc39bfcad403647f50a6f4e3e8a1ce17a6ad7e47b0f568160d08f933de3ee7619a97e97966808a08b091b303154c24db3abde226d18c1459f178690012475b1d4d02df74b030bb774429a4d0e349ffd3ee3be5a06efea10a00a7249e32659fb390462ede5cd8d4230e48e22c1eaf91b2fbb16783c504002833102ae72e28c5d3dc0bd37300240e4efa585cf381ab00d5716940892ef3ba3e1b7bef82f312ce77c30bd112f2a03bb92cf80f29988465d2af046fe27711a50619c393540af6acfe963482d3ed46ad80011e9e6a84553edc06238d8b79fc53008a822812d65991f186eda64aff8b89470685bd3ad8f0e0928dd45d743fc1c84b0f1ab8b9e724308d97dd9d0c0d14b2b8a2478870ee0450dd2151c3e3d74c6ed9d9fd4278000c77054b60dc435b9c0023474b51a8282260a4cb46c5ab6149fa36bb034eb57ca839358d97afa24b4b9ed99c4269660b1eec6351db069e8bad46ddc5bdb39c3aef27f6e464daab252bc0dda608cff0b81d0ee01087a4af1fcf1b061e5b21f53f0c2280cfca3170351face6acac795dccb89202bfb0ff22195e088b48362fab366daad34c60552df726ea8ae51a6d940293f0f3c948a7d691658010b2769eaf81b4b98f09b2bdb02994859d7334160c27e0002362b0373246d1f401bd32199b657ea61de2afda0855a152fb6cd6b5218316d38ccf22f24fd34d49ceb7f09f0aa5ca752130a27f6bd2b1f2b23acc75004f7ac6d0aa2a3d00b1c4a8d983bcfe6402b6c000029c4d04be75c52066f931e50ee74b8d9f7e4c83ddd5e68a38f85221c7d1443b0c9bcb59e096471c239a0b5c343c30cb6d77cfc1a7fadf1becf2d421d1151090f511d08d40f100315cf98f5966faee322108629c209739a5b63a65c6e7c800000463040b6ca5e0896935e1fde1c9090ce3152b4584c726dffddbb2df555c89a993a3e42e638cba7813cfa4708e73d4ecf049bef64e4e6a24452d3246ce321cd4731b9b01841113a046526f4a878a28a4611ab999d0fac3c3f05f6a8134f2a3f9f00c0b977712044f2fbb696d371549561d6f9b2d770ac37be9e74338103908b78dd18282c3d2d158113fd10529cc28425600000000000000000000000000000000000000000000000000000000000),
(6, 'eafan', '2fca191791af37d3f420b64f3ea0a6eb881478c520db96a37a9d2ac847e98e4a', 'ad45a92e7ae8a626a35ae022da4d3029', 'rtrtrtrt', 9, '2025-06-10 09:14:02', 2, 1, 0x89504e470d0a1a0a0000000d49484452000000cf000000cf08060000005281855f000000017352474200aece1ce90000000467414d410000b18f0bfc6105000000097048597300000ec300000ec301c76fa8640000284f49444154785eed5dc99223c7912d00894c24b6dabaab8bec16a5191329637174ac83161bcac8b9b449c7bad3a45f988ba4c318ff4477dceb2370c75d9f8279cf333ce1998804500b5058dccd9e45ee8b873f778f885cce5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c1a244dd3bb2449ee311947b1ee0e3805b93b4b78cf55a87e923cb91f0e87a7a20b97357207f2fc0be534cbb2e959eb6cda6ab5a42cd169a36c719b63379abb56a7f5af569bf70b3da0ec76bb32ad25311c8d269d4ee773d8c7e584e501649981407390670ee328d1cdd2c57cbb353beb741ec23ec7291de8a2dd9ef17e7bfd7c4907692f9b0fc72399067926d8c323d0890a2b9e647804e60448341f5f9c97c622869374489ca24c6030e9d11a0ca3ce44efbdd569173ae876e7fd7e5ff403c208383d1a8d66ed76fb27eec79d5d4e4758e14cc3668018048d84d34214184d9b64098624c0f234efcdd23c3fcae893e6e903228b441dd541a79b8843c16ad111c822d3bd5eaf2410ca7fb1cd88d2e544840410e22cc19045ca40a21469ccf8ea729ee4d9243db20633ef27cdb209ef4f234e899a7e5a019c06795832e53dee74d6a51078d0cfc3e1b04cd596600d0768a78848285bf0c2ddbc07025dccf2e1f0a88c85f7c3fb2279d8aea944dd9a7e2c79084621ea1304f20e8463161227cbb266e2106a3401963cbde1603ebabc9867c3fed1441fde87dc0f22ebe07c2cf7ca740dab2a50d2283485d374f7eaeaea91fac5b4cbb1092b16152ec409e9461c8638024d63e08dfbe3d17c78710e5c4cf33ce7b8c7c10bef030e61cafb228178af12796a7aa993c7aebbbebe96d209749c72874a65d76ad11d6d2a7e098134498838d2f6d1f60fd0c9d2f9e8e2fc6852b704e4195c9c4f1955796f728f26f228593a064a1e8d3e76bad56a4dbc03e18804c4910e0294738ee760ba1981242561504aea6608442f0d433b8ad48dbd87ec45e47d913cd23dcf7b0dfa68224fa75590853a65c9eeec2491de39ead93b108e4150919f51a98fdae54a94ddd23104821065c319a95b82863453376dfbb4b374d639f05ea64e0add74bb8f67390903228038e53d077d3491276917a461c4a14362491d934cd437f5ce73b81ca8b00251a18f240bbd22166d1e79807cd02fa7e9914920a63434b0e170386fc9a0e9c1a62877671c14ed20b2f6528da672afb6cda3e4b1249232441cab4f4dddd803876927d001cb1df36f1247238d12e829a037e5d88778d6502a46a3d114c73ccc8e033ef0d96e4dc52984f6dd6034947bcef37c490f0a1227b6bc0e1208e4f147780e541e60e032104a4367a9ded2a6709b400804f0383c861e673c1e1ff200e14396659581627d0c47f5f512504738cee13a9713167abb89f6ac29595e6a14dc9fd14b2319c8c3631f5cef120c5bd259d50b0d9df7b42ae23c13de797080720fc398a2944a54d2d048d4609e03eeabe421c2fc41451f121dd73ce17d105824ddf783c1a08ca8af05ea08baf7b6cf81c9032aac7ce8932541637949f42159783c250f97b1c18ce507632024baea46ef81f7f4da5187ba22d8f621590f2d3a9faa484a82522a8fa58246525ff654707f4b4092879e1bcbf7be71ac51873d85bc6e8d3c841289b0cb9f0bd533750302f9c3a30720d2d601a4e2ac1190383afd92e863a1440ae5dee7f7bc3e18f18c299a92458ddc4ebf0679081e8ff0e87300128c77a62908bd2b4b423b0f88d7f2ac4a1ccef35c38ff3e1b883ca2c47bd76b26ac5e6cf4792df05c3c2ea3cfbe3b97531619d741f96a9e731dacb1c130f63d3d91d7cd5156ee61172081e85c42fd78f4d937a157a3f162f2d5d2b255a87b69463b92764fd393d2b11024ba4e6f0b362d54677608a9ed294ad9d6d946ea11831aa01255534510781f0706cbae7b6bccdb04cfc392e7b2ce2c90d8a3cfbe08bd19306345edc2ab2a68146c0ceb7c38f73e7a57690bf2fa76e55c881a69a47d0578cfdb1e49f9ae8e7a54e6d72cb70d256b208d94344e7ad73d4add242ad3907711712cac6321582fd40faec37bdef64160b0e5336cb6e768dbb01edc0e30d260703d4c91f62575bbe7f558e2684ab56dc49c59208fb77dde5a50019f6f6e6e6440945e9f86bbabb4c49ec77a754e83c47b431e1a69bfdf2f7bd9489c5de94841f2502f9ca683e33578f47943b9bdbd951ea40f1f3e54726b62579e95e7e18023a769207a5e5ccfbe7856d1915e2361a3c02ea044d53a5227c3b60f4a8f3e6f214895241db186c1e8c3b24ea637c23ef42a898e486aea44c9bdebc81303b304121bd31e7d762df4ec48d92a837e6a144aa237c63ea46e421e94e2f1d5a9ec897e481e6ffbec5a982b43e9fc52bf54024943c350f2a8877d63ec0579a08b923caa1725d15b422321e0d1679702f2480f1bc943681ebf0f4661b057e451e210fba027edc60ed7b72f3d93c72d8c3aeca9614701662ba081904c7b42a27d681097efee58f2d8e9b7069d204a4fdd7621ec28407ac62f762e558492a7befc0dc16ef43779490e7ae079cb4f0bd3a1ec136914219df4d46d17727b7b7b7f7373c33f959579bc8d36fb642024f85b188646674c965dc3c49e446481d65968af7aeab60b617b0706b9948a285829fb40206d87e15a766e18204cd9cb66bfcbad7ad9a7e84c07836bf55eb71d083df8641fc8b10ebcc6803721cf70389c1a025722d0be407b470990c753b72d0bbd53656c675fa1de1d86bbf30631bd38ffda66d3343b4d32e9f45b41af818feb505780479f2d8a441d60a922f6114a1e9630949d7955b677783eebd5094b184ba4b7864d2ba12b7fde6d4b52461d35cc7d861a2b0d15d865ea56f9661d618943ec0b79785d9a4e86711f8f3e5b90c6cf49ed336818c4aec90394e4a1beea64d9171dda7618bfbeca1291c8db3eaf28e5575f305d8e4c1f02f4fda2b7208f9246816525f6813cb1fa0cddd61e7d5e51ca6e57a66b8790b229943c28df843c7592c496bd15b44dc6ae6a251297853af6e8f31a422f446f84c9f28d4ded82dd7728795a6f98b6596814da0702e935f07a481e9d6749678965bbd2d7d18af41cd91e19621f2abf11e1675884fcdb13a5441efe0f6737728f734eed754411bbf61d83f568eb92d3743848e53c757ba9d0fbd00ba90757d05bd9f9bd823150fe0c8b25ae7f8610ba2b6378c039e51fa32b11bbf61d83f558af4b4621b683e83431efa9db7345533655b07aa943208f461d82bf636ca53b78673f45a4eeb426e57f45572176ed3b06eb916d1c1b7d082e43b9f3c1e5631249d9ac62eb24da4b04e3b406cc9f00b7d364c63f4f639bad89389b0eda87e1bc2b11bbf61d83f5c83a5d519f1e7d9e29e503a04a9a358ade0fa8719a5fcff357f4ef6e3fcc933cdb5af491270b92cee4fafdbb325d5c89d8b5bf1156d4a9479f6788441d0de9218c0bea8f9dec1dd438411e8d3e4cdbfae3d1bcdbcba6499e6fa5e340da879df6947ff03e94b4cd82f56c4964dab91e7d9e286577ab124715bbf7ddd4c640c5884122fea2bd9bf7b64e9e4eda9df6fa7925ea352276ed6f08258fd6b33a49ccefb29bff2884a15a52b6ba320f893c021a3248c4d4ad9da55358f9760cc1449ea56b882176ed3b84661576597d9ee0d3e1283d75db5018a219aa9714791008c6c9764702c270ba371c48a741abdbd93a7918edf4bc2b11bbf63d0289a4e37b98f6a7ad379432653b481803d5863ba38e2c83716f6db014c795271910e90eadc3a0091a8950fa13071b4a99b21d248c8196633d6accdb7d4ce71ec491c873886d9e2670d094a91bbbe131efb2420e3b65238c8196e9d3c298b74e9e8da20e11bbf63d820e4fe8f38c4cdd507aeab6420e3b65238c81460c79ebe4a99daf19b16bdf43684711c8b44ddd1d851c1579ca88b3abc883e31f4be4516804eaf57a4e9e357234e4b1cfb6b1a72d106827e439c441d23ab4b340c7f910819c3c6b443a0bd4db1c248271562240986e25f2e9db6d357c377fae8d885dfb1ea14e1ed8848ff7ac90c3ef2c88408c00c6aae5d9761abe773876a9bbfa2b1c870c3a52f34896771a34c8e1a76c359030ea41cdfc36d28f8aeeec390f157a0f41673aeda95b839406702c956f2b9ee0a3455b32805277f4d2079df61aa8ee4ce9e46910f9fb012bdf1adca1c21ab04e933cc0d6c8a3ed836381254f7816cedb3d0d22efef1c0371086bc8fa302b49b42df2406f12798863893c5687bca7e058bddd63050625efef605214651a88070b5bf1f67eb6451e189790878fb31c0b79ec7dd0a952a7e13e3d7533723f1a8dca6f8d59c33b5468c5d70d19f3db483da27f803b26f0bee818503a796a22295bbfdf3f8aa843a811b3c2ebeb007e3a9804a2113c19e10963057557fe01ee181c8f45ddf93879aa5249d9f49bc5c70e3a0ba62031040329c1795d077208b82c6c27edc43a788e43863a0175a6b8779d77f21891c6ae56f8310df06d02de370d8368327add86064584f4652562c73924e83d68e4d612cbbdc74d8529c86030902e6acc3a1a6089b10962c738446804528711ecc47bdc28699a3ea0ad53799eed982a7f131c9bc1bf26542f563f98f6d46d381cca5f9b11794ac510a71285943475c4b63d45d41daaea06a59327cf73f9f16cfd43ee56698e38d4989a10dbe7d060ed40db7bbc3794deee51f298576d4b653956c3122586d83e87066def686709ef8b6d9fd0fe39ed760f48f300c8e01e714a9d064d46be6ef9a6a8ef7f68e03d90249c56e2e8f280d34dddf8480edb3b1c18c5ac781755962acae168c249930744299fa2c6ac1046735c278f631d6023a7dbee6117350854a66c164e1ec73a848ce5f4da3d9ab29d9f9f2f29c5e1d804b0a1d34cdd98b22145abfc2ed1a38de32960ba7fd2e4b1bd6bdaded1d2e158053adb93268ff6e3134a1aac2b97391c6b70923d6ebce10a79346d632eabcb1c8e2604db71f2d4a38da76e8e0d71bae45192d8084478e78163439c2e790051829288a513c7b1094eb6c30052f9da8b12c64e3b1cab10b295937ccae01e372fe4b1ddd576dae15887107d4eee29037a0b7934c77616e8b4471fc7260899cae9a46e7c3487de4209a2ed1dce2b79ea1d080e47136037a793ba81184bdf2c204818254d357de376312cf6759c1e6af67312a99b449dfa370baaa89384d128868af21c7b86f6596b092d2c572cd7731dcbc7b450474b1285cea7a34fddca5eb666a8f2ea646134523879f61d9628312ceab909cbc76c021cf2f193076d9acaf84e1c7525c648e4e43934ac27cff23eebc0a8c3b632cae36ff7903c59964d7bbd5e541905ea4a75f21c03b6411e7d0e32a470c7ddee217936ff3a685db975123d4fe18eb707a3456cf94b70f4a91b3c85f4b46132aa802a5691c78973682061428a25886df314688701118e7dbca91bc7771079d6f4b4ad822512607f8bfe1c44cfe17835a89edb8832007faddf4e3a25a2fb3c019ab2f16d6443a4e34cdd98b2b1a78d374d4f8145cf44f05a9608cfc1d2711daf0aea38429c4e371144f7790234f5af39e3e34cdd943c28370edb3634739f96317aa98040044eb38238ad650956a09d07649b701cc7cba1299938c5409852d7a89ba4974929cb41a06e1f0eb453ac6fa32474bad3c1363866bbcde316c7ae9fcfc2da0870b4ed9eca4f679f8a2461ae5c28344d4140867e4c4b05810c59de9bf7faf93c49bb0b02d52ab2049745cee17805041d4b94c940127572a893ee20179c75d1f64916db5ab08ebb5dfe7b743d79b88eced82c3b5ef200e50b70eb400f44052a64b92a394c4bc59028204317e449419e36c8434f2704e1bab0bedcd71ec3f16ce853034beba0ebd279a12481489874d89f9fe568a730cab03e810e08946667f3bc9fccfb03a461a67e9ac943fb218af99322cfba30dc082a148a4f33e6cfc57c990e04852bb88c209108d9a64ea0d8391c1b63315e53804e91ed10cd00f2d130382eac47a670d6c534899376e6a3ebf3f9609ccdcf2fb06d0e12325d0b75cae9cbabd15af2e8f29349db0093b6553d481d59860882542deb21474e0bc32771862310060aee0ff3796f389068431231f2d0cb115cce92cb89327db0048a9cd3b139ec802761c9930ffa65bdb4508f8c381dd4573acc67ed416f7ad64ba78838d3f38bac044833bdb81acd7a79e10c97c9a3f652254f2d9371f258d0134199332853147cfbc5cdf4f6cb9bd9ed971f8430c4f8ea72de1f8fa4b2186944f9217de3fa72b9a67044e45c8ecdb1fca06761c8daa3c63ac84683797e752e6865c9acddebfe749627f7e3ebf17d3e4e0ae467019cee3cf47ac9e3a75fdcae258f92e6e4c853e4a9aa88f2c62bd068d3e9b4f9fac24f4972767f7b7b2bc887f90322cf241b0ca6a3cb8be9f8ea62f6a7fff971fef1975fcddf7f713b1f5e9c4baf8e12c823cfebc31247002317c041699b876d9d561fedcf0c29742f9d75f274ed20260904e2d059ae248fa66b27d5e601eade228aa48b921590b6a6240e9655647875550e86813cff37babafcf7d5cd7bc9b7cb080302b1f78d24b2bd734e9e97c312a7d32a8c99864c7d13a263d4034883f60e740f02b592f623b67b384b9b07323f7dbabdfff88b5b6619a8c382408bfa5a9047c779386e487b0a243bdae7dba2e4293c16bd48504c505692a1e1f86e301f8cba5386776c1b95fffee187cfdffff8e32307cb481079e814c41185a2f258a9924a8492cb3721afe38508f5c83aa04353e7d51f0d672827a88fcfd86e4912a46fedac35cdd0f6e9f68bf44f4814a2196da4d52ea20dc96aeaf2a89fac2ec9a30361c4823c21950b4a7ff7610c0c5792a7dfef7f86021fe985a848128710e2c8710b1259e872ecbe04bb7d6cbd6373a80e5937fc1d089d97ae1b8c86d435a3d01281e431ae7e32195d0de72011b207ec53b47b43da4d1b298eadf5c912fb1d6dca4629c9635118738d3cf034837177fe9f5f7f39bfb8ee4faeae864ba1988a670560528ea35e88c7e3b42e2f8ebf802eaf83eb58c1d26364fedee07819a8d75a8428ea582248374aa04ebff3b99b278fbd513acf864cfb8a7d8acea0823cb62e596f983f4df20869943cf02eec8ace871d12e8f1f25d7f59b950388c9c8a979c979eadae4c9d6e82dd5ee7b99f93677b20818444244287e36f7c4c27413b255d728e69de7940f4990979740c48c993a00d6bc818a68f9f3cbc516904861baf9387b92d0741ffe3eb2f67c3f368ef0c15cd86a1ec6f9548d8a8b30ac5755409a4cb37219f6335580f746c755d4a7dc141a6592e4468b7bbd3b3e20de38ab0edd34a4108469d401e7600719f4ed68bd5dd69441e25cfa22b72411e362c931451206d4dd9f7cf1d6b22c7618440594113216278cab68ee7813a2689e27a86fe1179d2ac17250f08738fb6ce543a0b526ccff68e741a60bfd06120445c1cf3b4d2b626f274b33611eda286c871d4a35181ec2458152d788e7a05c69639b603ead91a7aa177d43552b74dc8c34c447beb0ae214c7aad5f96990673100b65024c9c38e038e4eaf264fe701dea77c1bb55e29f5ef237099855db7c97ac7f3506f37d6759b74b91e91294b679d4e243d47ddf389925e3f8c190548ba57234fb081e3260fc852460c1287650178a116df0c44484668bebc1e3791e7ee8cdf26468311d32b5127451db17d1c9be3a5faeca67472307a7610c5bf372de421613aa1b7ade8aaa6fd2c526e966c5ba13c0df2287116048232e4ab380579aedf5f0879226d9e7b441d2874116d9a40a5ae426c1fc7e678b93e5987cc30c469c60cbf200fb294b457a46c31f228307ffce44189705bdc38d3379685228b5c9669dbfb0f57f38beb9193e70010d32d11dbb68a823c61fb28795a6d385bb477f8343de6c3b6057938af08e73bda477328548e904751bcf05628d192e7ddcde5bc3fc8e2e4e1313648db5e8a50a95a318e35b0fada44679d4e916970bae1e900210f230e4ad98eb662f73338fa8f1e56c66788e2d5ea2a79d8abc236cf4af26c10795e0a5e57cc0836358e5383ea6573fd14f5cef60aca95e411609f15e489ed7f7442ef50f69459f2689b87796d7f98cddbddce8bc853afcc3a62fb58c4c8c3f9a2028b4e0fc702aa57eaa7a8d3f8768a76e8720efb45c903d24c197534f214c72ff6e3381fe7b91c3809f288f16b5b67f18068d1db26f92cbc0c7b57da1df9d2ce9b9127b60d8d82837eb101da5387ea7553f22449a86f4c63bf959187afa7687d68e4b1e7e1279cb93d773a6611e3d747682c79a814514c08d3a2b8e5ae6af146ba0de61ba195d984d83eebc0ca22718a5423becda9823a558356a35e0d38223eab8669ecbb6cfc9db387a4d7e2eb0b92a16049b10f48d79531a2457680f234c81314a54a0b4a2920ddd8e5e3e7d1507c2fcb19b9b08d8c3a4bf765d827a07cf76315cc799b4092d41f2fe143a8f5815882db848adcd078de16f61e78bdc51082ad0fde431316c76902872188458f6ae12cf96d0a990ff5c0777d1081ea3d65775837e9f68aba55f2a4323644c75ba46e5c165e41896529472765a7012baa5e6162804a9e56a407850a0279e43d0f2a159eab7c6c83848910a911e19c4d08036fe57c9e7364bbacac72b942ae3de010c8439c9f9f4bc9687a7373235fdfe4f5176929efa109f1e3c540f2d0f89548420494eae07a796fd649979e305838c9700c9eb78838c922c5c73a3ab353210f453a0dd4dbd50d8de411025161f03e58b6f048e9d95d2be94ce441414b84802711c89c3306db2065f9f1e3c7f9edededd2760a258e22b6cdbee1eaea4aca2fbffc9211f6df5f7ffdf5d2360bb09e14b1f555d423ce62401c30f5d0a2e1e7f952ca86fa9f29790a14291bc9d34d245ac9726606c004ceee68c778ac505192ba450d0d0a33d1672975bbfbedddc3bbf7ef661a71ea685abe047bce06686ac328f4a73ffd89d1e7df243c2bacbead25ced23ded29e8b8885ffffad77c8dfd7f597279fcfa9f4a1e3ac7b81e34ea7cf18b4ff32ccf26b75f7d5571909d6439652359943c6c1b17bd6e92eacf80a31ee3b1b2f4d9dd4a65d1b08ba8c3722975bb8364fd7cf2eee67d590915c2bc52e4216cf4190c7a30b0deffc24b3f6a4a6751dff75080e833036944c72c712fb3e17018dd360e25d372b948ff68e45d71462c596ffcbe5babdd7a4cfb69e565c74e7af6d04e50efa823f6ba2a014916254f714cedae3e9d948d52f995bca24cdf82719be8b3f4d805a3cf77ff7537932fe58892d1a80f447a2df2e8f530caa0d267df7fffbd1818d2b7077a3b258d42f73b14f09a798f28a7df7cf38d181fc8237563b76b4661c0ab9065798810456f6ab90e7584a8b3449c145127495b93f1c540ea486cc09cb33846b5b3a0d53a9d944de5810669d39f3a79ba19d651818c3ecc818d68f4f9eeb7770b258768d54e5e873c9a2e0c0639095456d0a74f9fe46f0fc1f04ae87e87025e3f3b410259acf17d46e429bf0dd18c408415287ac78a692511c1880307b4fc7a3da24e276dcdf83264533d2d4828e439a9944d8461169536d51e2ca234406be080f4ac7596a3cfb7bffdf6732fef3d9e5f8ee749ba48db4cc45a8d70de26b0c14be0ba2a15cd6b57f2580261d54181d7bcc2f878bf2f2210db284a184ee739ffa3c375adc7db8f1f9788a351271f203563fdd01912380fae514aa2e8716354cb88938b3af27921549ea4076a7834448944c6c08763281c0a1c8efb333424972a990442f4791c9d2347a7a2b14f871f14476949542714a39a461682630fb677489124cb1e52c9c3cae3356391c012e850c884eb8c8da5a97c86ae1ea92ffd7e349185d7038afae2370a16e99812a6e8095b449ba2adc2377e07d18843e9a41db475dad2d6198cfae5f9b04ac0f68dd53780f6f089451d230f30c4996d948b8781c22ac6ce69be0cd5454576c4235624e5b7dbbaed8240619fa5d40dc420a99458029ccf12c8e2fc7c846b3a43452f9f8fe4c1354bd4b41ed1a256c97b09767aa05c451e4a49207efe58bfe29af3edcef258c5bd9228d447419c6239db24057948287e2db4dac65121a1daddd6633ac8ca3a2a3b81e4d88b81677d437530e8afbbf6a39632fa547e8d172288a662498e92cb0810081e6aa90218813a496bd2ee148f731024205fe7b63f5162ef8dcda7fb9a2298e9f0ab8b287128240f9fa5e23517bd49d8be862652ed17c418d71a20da219ff9f1f56e8a7a1a2e2210c76df8132a12843f1bc3a62518c955071cc44c127e26ac8138387e2b4384efe11852cf5a3fdc7fe184d4c10ef99f9f62d9522a7f52020533ecce46a351a9a48c3f4062e530e2148429c973f1fe7cce8fe1f1a378dcbf221c1fe89c3db4da85a724489c4ae37305e4c95d94d8a7913814449c7b184c499e588a7638e4e1b720d6a73e34701047f4ca9f515157fa217eac9692515c2253986779758df66882fa6a4cd50ae248bb96fa0f1987fc6581110bed1bd52f234f9e1751a7d7cb66889c279bb2a9c0e0e5b9265112c3bb449c60c812c239cdcae2778b51f22378ed1e3c55240289c0f04920461da944390e148e5443de85c7315832f56065eb4f9508a66ab1d4d00ac8f380c8332b3c6ad5e32a0e216d6337320db4ddf0d5ceba94040a75a3ce866054920fb387e5a3b13cc234cbb264b22ee2e4631082c70a50e22879582a817afc687c71fda71d755434fad05b8bd1a1022c81caef151341c1efbeb89eb725856b3074122839431a7756edf654846313ac74bee6bb0971e0ed3e8338f2ff9843ef3060435f1bfbad567374a808f5da3a9b802033a670743c447f201d2ea843f642f2a979f990fb43534f18ebad0b07387e87148c7541e275a1334ef37ab4972e9445dba9b86e461d94271f7554a4ed43f260ba306834f8759c47da3c1a317a30d690ce317a08819a0dfe0edb3ef0510f1c870f190a1081a6d84fa659d10452c4c93ae2d0b8988268cf5379bd00c97208d1a68a36da23c392408c404c856e6f6fd77974d12b49c40f7410d43153667eed8860b773d8b614e98ac63a6e07fd4904eb0e0261807c1c8844b2b05bbb8594b8cd48537de29bb682d2a38e9107867994a5322b3d663a5fe6c4c5b2d1791fed8e162afd0c5eae41a1c572368aab28de1552acac0c250e074cd9a5cdfcde46974324cf823485776724bdb9b941aa954d9092ae8f42810c44d07154187dd21451286b4ddaed169c55d1a993e6d017eb9af51b52673e2592f68a548dd0b40d8791f6252210c79ed65fdb8909952f6d1f8bb24d4105a3943690aee7326038427e8df48cde8f242a3cdfeb0d9c29716cfb463da125501dba7edd76cf45fdf8756cb2bdae53e2f3be3e7cf840124914c23ddfb38384d844a74a26058e876330ab68cf6e3e5c155fc109f5c6de3a210faf81d3e15a2cd8ae34f3a7f734c11344da3e8054222b94ded01aada2f0fca8744422e6dcecf961c58cc7f90ce5b4df4f27fcca3e3f162e15c912688c4e4186c3f42ec9833795cae73531b2f1a5b85446c975c00f9b2f216698db823d570cebb6b79192fab6dbb22711864b63e560b000049ab0b344c9c4ef4b905c04234b927424b274bbed29db3e58363d3f1fcf842438264b820f7a9a867f23700e29796db483f3f3f3d37b9ae00952469ffaf80915682b98e461faa45ecc823d681cb3c9fbe92cebb1f2f93440013efe51920ac8c73002c5307dc8905af0378e04db42a8ac22951490b0bc061a5d953c6a8c841aa75d5fc7baf59b40cff354e8fe75f2d49d941a2d8d9864fae28b2f9836cdd84d9f656940574882fa9831a5e5b88fbebba3e92dc77c380ed4f47a82a2e95ac30b7b1e753690f28755962c6a985ca695ce8a52c2b07b945dcf63b48108a6724a2436f0199d18a5ce2f1039d216f2fa824c8321bd6a31fdfee602a905bf1797166318e1dc342a469e05698aa785753d612b7b5fa0d7d4746d56bf3aafe03d13763f4e7319c9341e8f257af4fb3d21c7629ba25e48162ebfb818cfafaf2fe5e15a7176613b0b7b8df67c7a7d74a498f6a8b3894051f2e32a7a3b250d1697b05189a440749152894470d9688c4a06915892585c4652e8f8c4e5557f7efd6e088cb15d8ef538170846e8601fbd25cfc76b50e3593ccb556cd3043544bd076b18bb8035c8d8b9d53863a8eb9c5dc5240d754147520c10f3e902a6b299908551a6cc08cae3143ab4c7d2c854bfbefa356af734ae65b36e749742a82c28b37caad72ad6928724a0b12b69480c128444d16575705de86410d2d5074a4be0f885312c0ca92044419e58855bf03a898270f58f6bbc1c7afe2658d212b16310ba9d5dc6ed4916a66d244b45e74f00f567c9a3ed1e4e53277a7dbabed86671bd58efc4798e5802d9caa531b2a4e7b35e8e95420fa895c375dc86e90351f180dc861549cf1808a4e076ba2d8fa1e7b360e5c62a9ecbb83d0d4e49d364242f058fb70a3ca79e97881d83b0dbf25a79ddb17b56701d89c592fbc4b66982bd16bdb6fa7a1e9764c5b413e7852204b24a6605eb348d9bc4a89388f34aa226d8885581ae37c7e439adf75563b3d7a515cf7483690de72d74bbd742fdf875e835c68c94685aaed0e3c4d6c5503f1e75d6b47fd372ee13229d8fe7bc86d0fbc0201fe9ed305b7a264e2b94444a18e94c30ebb7091a020d8715afd756bfbe6d408d3566884dc6a958b7feb5a03a899d8fd7cfb450e7491a96d8d689f39a4202011c67900732b10815538c17d423cf5b80c6a1045283896df79ae0396346a9cb9bd6eb36b1e5af89fa39749ea53a42a23610ca313527ce6bcb575f7d75f7f7bffffda7f178ccc7d145d95a1245f769d143b30bcf5f078dc222b6cdb6c1f392c44a648d4eb16d5f0eb6779ad1eb9114c5343b59ecc740085e9bada76fbef966f6bbdffdcec772b625fff8c73f1e7ef5ab5fc98743681c58249e4b3fde4758429d1a943c1afdb64ba02a5962206916df2ea82f93e370105a06a287c3e1ec0f7ff8c34f7ffce31f7d3ce7b5e59ffffce76740220c6619fa679797977c6ca47c0a40db1b36976e46b5a2e3db1c16f68d3c0a12c6469d02adc7dffce6370f04a20ee68540f3dffffef71390c853b7d71228f733228e1804943d45049a50e9d7d7d77cceea0191471edca4a160f30d612bf229fbed2f943c4aa0ed1187a8ebaf0a7dd98ed0c79a58b65aed19ca095ab22541f8bd38a66ca8536c77c63a7e7402bd827cfbedb7bf84fc4cc59230fc401f951d568bc050f8e4339f8b9b69645a8fe50a2f10db76ff4052c488a1cb9bd6eb36b1e54f434c775530dae883b4fc861b5fba436db15d134dcd4818409e67037e66dd87552ecf1592a54e98baa0adc357baf98af4e3661168b9b20bc4b65d8f4d8cf635b12aaaac3bffeb5c5f4c770bd8c8737dfd1ee9746fa39e34b6791085961ca4cb0e8404425169f7d058d816b2a4d2ef316bdb40976b8743ccc0b86cd5f2d8ba3a34a58aadb3b0c78c1d3bb65ce79b9c879e9b68229f6e637bc2b88cb0cbeae0fac574679665bd2988c3a7a1e75f7ffdf5ec871f7ef09eb40390fb90baf1ab3c531848d9a14042d931061a0f9f06d079bb5ca7d568482a124d977359bd9da5866b8dd31ecb82eb5721b6cfa6d0f3369ddb82e75242c5b6b7f7ac588cb5154f0450af380edf420561f89a341d58c2e8c1d7ba499ef95ffffa5727cfbe0b22ca1d2af167542a2b8baf58f3cbff1318bb1089646165d328ac619070fab327a24e8ca7c01aa1354e4e6f62d09bc01e578fbdeaf85ccef57adf9c5f772dea34745e1d0fcfc775389e1006c7910f7e60ddd22bed88389f2f2f2fe73ffef82309e49d00fb2e171717f586e61d0c26bc169c4c40a0292b1d302fbb2d4083a171d048eaebea46c76935649676dbd7829ed322b69dc52a22ad82128cfbda7be274389ebc108779210cf58a652bdb2724cd77df7d37ffdbdffe4602795be65005c41022299990dad108e44f75340e9bd629684c2414a186c5ed1531238da5750a6ebf0ef57d5681dbdbeba99f538fc9e52401af4bc1ebd46be5bafab97519a3c75ffef297c7ababab07946b09539740a09f11899c3cc7222413bbc0613c95b1223b1d43ddc81434361a636c9da269dfa7c09273d3e3713b2550643dbf1bce14ac044832fdf39fff2cd119f3334cbfa8dd82c8e35dcfc7281c6cd541ba8f1f3fd260f81de70a68404a0c1aa10597d581ed4b6365c979bb6e15749ffa7eeb60c85bb9071c638a6331dd1270daccdb14ec9e914541c2a0946be03cd6bbb8548583af9f3e7d9a03f2d8080d498dc9403a1f688804e61bb1c936aba0c66d513f1e97315ad865011c30d606fc2658994a81347cafea674c7acae5b22c6150ee673e0a542c69146e1733c07dc2368cdc532e9766b9bdbd75037171717171717171717171717171717171717171717171717171717171717171717171717171717171717171717171717171717171717171717171717171717171717171d95f393bfb7f1ab57f51bec01c820000000049454e44ae426082),
(7, 'nekit', '9dad6d5ed64d10742efd7b2e56d60dfa9a1a1eee361e71acf654e5afa9d64a53', '5f6dcf14c3205176d99a47c845c71060', '123', 11, '2025-06-10 14:05:28', 2, 1, NULL);

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=288;

--
-- AUTO_INCREMENT для таблицы `AnswerTypes`
--
ALTER TABLE `AnswerTypes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `Candidates`
--
ALTER TABLE `Candidates`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT для таблицы `Categories`
--
ALTER TABLE `Categories`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `Emails`
--
ALTER TABLE `Emails`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `Employees`
--
ALTER TABLE `Employees`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT для таблицы `Interviews`
--
ALTER TABLE `Interviews`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT для таблицы `Organizations`
--
ALTER TABLE `Organizations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `Positions`
--
ALTER TABLE `Positions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT для таблицы `Questionnaires`
--
ALTER TABLE `Questionnaires`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT для таблицы `QuestionOptions`
--
ALTER TABLE `QuestionOptions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=110;

--
-- AUTO_INCREMENT для таблицы `Questions`
--
ALTER TABLE `Questions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT для таблицы `Roles`
--
ALTER TABLE `Roles`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `Statuses`
--
ALTER TABLE `Statuses`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

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
