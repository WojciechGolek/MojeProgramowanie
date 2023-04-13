-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 13 Kwi 2023, 10:06
-- Wersja serwera: 10.4.27-MariaDB
-- Wersja PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `football_league`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `matches`
--

CREATE TABLE `matches` (
  `id` int(11) NOT NULL,
  `teamA` varchar(30) NOT NULL,
  `teamB` varchar(30) NOT NULL,
  `goalA` int(2) DEFAULT NULL,
  `goalB` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `matches`
--

INSERT INTO `matches` (`id`, `teamA`, `teamB`, `goalA`, `goalB`) VALUES
(1, 'Górnik Zabrze\n', 'Zagłębie Lubin', NULL, NULL),
(2, 'Legia Warszawa\n', 'Widzew Łódź\n', NULL, NULL),
(3, 'Wisła Kraków\n', 'Jagiellonia Białystok\n', NULL, NULL),
(4, 'Pogoń Szczecin\n', 'Lech Poznań\n', NULL, NULL),
(5, 'Górnik Zabrze\n', 'Legia Warszawa\n', NULL, NULL),
(6, 'Wisła Kraków\n', 'Zagłębie Lubin', NULL, NULL),
(7, 'Pogoń Szczecin\n', 'Widzew Łódź\n', NULL, NULL),
(8, 'Lech Poznań\n', 'Jagiellonia Białystok\n', NULL, NULL),
(9, 'Górnik Zabrze\n', 'Wisła Kraków\n', NULL, NULL),
(10, 'Pogoń Szczecin\n', 'Legia Warszawa\n', NULL, NULL),
(11, 'Lech Poznań\n', 'Zagłębie Lubin', NULL, NULL),
(12, 'Jagiellonia Białystok\n', 'Widzew Łódź\n', NULL, NULL),
(13, 'Górnik Zabrze\n', 'Pogoń Szczecin\n', NULL, NULL),
(14, 'Lech Poznań\n', 'Wisła Kraków\n', NULL, NULL),
(15, 'Jagiellonia Białystok\n', 'Legia Warszawa\n', NULL, NULL),
(16, 'Widzew Łódź\n', 'Zagłębie Lubin', NULL, NULL),
(17, 'Górnik Zabrze\n', 'Lech Poznań\n', NULL, NULL),
(18, 'Jagiellonia Białystok\n', 'Pogoń Szczecin\n', NULL, NULL),
(19, 'Widzew Łódź\n', 'Wisła Kraków\n', NULL, NULL),
(20, 'Zagłębie Lubin', 'Legia Warszawa\n', NULL, NULL),
(21, 'Górnik Zabrze\n', 'Jagiellonia Białystok\n', NULL, NULL),
(22, 'Widzew Łódź\n', 'Lech Poznań\n', NULL, NULL),
(23, 'Zagłębie Lubin', 'Pogoń Szczecin\n', NULL, NULL),
(24, 'Legia Warszawa\n', 'Wisła Kraków\n', NULL, NULL),
(25, 'Górnik Zabrze\n', 'Widzew Łódź\n', NULL, NULL),
(26, 'Zagłębie Lubin', 'Jagiellonia Białystok\n', NULL, NULL),
(27, 'Legia Warszawa\n', 'Lech Poznań\n', NULL, NULL),
(28, 'Wisła Kraków\n', 'Pogoń Szczecin\n', NULL, NULL),
(29, 'Zagłębie Lubin', 'Górnik Zabrze\n', NULL, NULL),
(30, 'Widzew Łódź\n', 'Legia Warszawa\n', NULL, NULL),
(31, 'Jagiellonia Białystok\n', 'Wisła Kraków\n', NULL, NULL),
(32, 'Lech Poznań\n', 'Pogoń Szczecin\n', NULL, NULL),
(33, 'Widzew Łódź\n', 'Górnik Zabrze\n', NULL, NULL),
(34, 'Jagiellonia Białystok\n', 'Zagłębie Lubin', NULL, NULL),
(35, 'Lech Poznań\n', 'Legia Warszawa\n', NULL, NULL),
(36, 'Pogoń Szczecin\n', 'Wisła Kraków\n', NULL, NULL),
(37, 'Jagiellonia Białystok\n', 'Górnik Zabrze\n', NULL, NULL),
(38, 'Lech Poznań\n', 'Widzew Łódź\n', NULL, NULL),
(39, 'Pogoń Szczecin\n', 'Zagłębie Lubin', NULL, NULL),
(40, 'Wisła Kraków\n', 'Legia Warszawa\n', NULL, NULL),
(41, 'Lech Poznań\n', 'Górnik Zabrze\n', NULL, NULL),
(42, 'Pogoń Szczecin\n', 'Jagiellonia Białystok\n', NULL, NULL),
(43, 'Wisła Kraków\n', 'Widzew Łódź\n', NULL, NULL),
(44, 'Legia Warszawa\n', 'Zagłębie Lubin', NULL, NULL),
(45, 'Pogoń Szczecin\n', 'Górnik Zabrze\n', NULL, NULL),
(46, 'Wisła Kraków\n', 'Lech Poznań\n', NULL, NULL),
(47, 'Legia Warszawa\n', 'Jagiellonia Białystok\n', NULL, NULL),
(48, 'Zagłębie Lubin', 'Widzew Łódź\n', NULL, NULL),
(49, 'Wisła Kraków\n', 'Górnik Zabrze\n', NULL, NULL),
(50, 'Legia Warszawa\n', 'Pogoń Szczecin\n', NULL, NULL),
(51, 'Zagłębie Lubin', 'Lech Poznań\n', NULL, NULL),
(52, 'Widzew Łódź\n', 'Jagiellonia Białystok\n', NULL, NULL),
(53, 'Legia Warszawa\n', 'Górnik Zabrze\n', NULL, NULL),
(54, 'Zagłębie Lubin', 'Wisła Kraków\n', NULL, NULL),
(55, 'Widzew Łódź\n', 'Pogoń Szczecin\n', NULL, NULL),
(56, 'Jagiellonia Białystok\n', 'Lech Poznań\n', NULL, NULL);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `standings`
--

CREATE TABLE `standings` (
  `id` int(11) NOT NULL,
  `team` varchar(30) NOT NULL,
  `matches` int(11) NOT NULL DEFAULT 0,
  `points` int(2) NOT NULL DEFAULT 0,
  `goals_scored` int(2) NOT NULL DEFAULT 0,
  `goals_lost` int(2) NOT NULL DEFAULT 0,
  `won` int(2) NOT NULL DEFAULT 0,
  `draw` int(2) NOT NULL DEFAULT 0,
  `lost` int(2) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `standings`
--

INSERT INTO `standings` (`id`, `team`, `matches`, `points`, `goals_scored`, `goals_lost`, `won`, `draw`, `lost`) VALUES
(1, 'Górnik Zabrze\n', 0, 0, 0, 0, 0, 0, 0),
(2, 'Legia Warszawa\n', 0, 0, 0, 0, 0, 0, 0),
(3, 'Wisła Kraków\n', 0, 0, 0, 0, 0, 0, 0),
(4, 'Pogoń Szczecin\n', 0, 0, 0, 0, 0, 0, 0),
(5, 'Lech Poznań\n', 0, 0, 0, 0, 0, 0, 0),
(6, 'Jagiellonia Białystok\n', 0, 0, 0, 0, 0, 0, 0),
(7, 'Widzew Łódź\n', 0, 0, 0, 0, 0, 0, 0),
(8, 'Zagłębie Lubin', 0, 0, 0, 0, 0, 0, 0);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `matches`
--
ALTER TABLE `matches`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `standings`
--
ALTER TABLE `standings`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `matches`
--
ALTER TABLE `matches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT dla tabeli `standings`
--
ALTER TABLE `standings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
