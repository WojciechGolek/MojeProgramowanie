-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 11 Mar 2023, 11:08
-- Wersja serwera: 10.1.30-MariaDB
-- Wersja PHP: 7.1.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `room`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `notes`
--

CREATE TABLE `notes` (
  `id` int(11) NOT NULL,
  `roomNumber` text COLLATE utf8_polish_ci NOT NULL,
  `guestName` varchar(30) COLLATE utf8_polish_ci NOT NULL DEFAULT 'unknown',
  `priority` varchar(15) COLLATE utf8_polish_ci NOT NULL,
  `description` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_polish_ci NOT NULL,
  `timestamp` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `notes`
--

INSERT INTO `notes` (`id`, `roomNumber`, `guestName`, `priority`, `description`, `timestamp`) VALUES
(11, '7', 'Jan Nowak', 'normal', 'spalona żarówka w przedpokoju', '2023-03-10 07:27:31'),
(12, '7', 'Jan Nowak', 'normal', 'spalona żarówka w przedpokoju', '2023-03-10 07:27:31'),
(13, '8A', 'Ewa Lis', 'high', 'cieknie pod umywalka w lazience', '2023-03-10 07:27:31'),
(14, '8A', 'Ewa Lis', 'high', 'cieknie pod umywalka w lazience', '2023-03-10 07:27:31'),
(15, '2', 'Dawid', 'normal', 'Brudno pod łóżkiem', '2023-03-10 07:27:31'),
(16, '5', 'Bolek', 'normal', 'Brudno', '2023-03-10 07:27:31'),
(17, '11', 'Jan Nol', 'normal', 'za ciepło', '2023-03-10 07:57:16'),
(18, '1', 'AD', 'medium', 'Strange smell', '2023-03-10 07:59:10'),
(19, '2', 'unknown', 'normal', 'Spalona żarowka', '2023-03-10 07:59:54'),
(20, '11', 'John', 'normal', 'garbage', '2023-03-10 08:03:50'),
(21, '9', 'Lidia Kun', 'medium', 'Smells not well in toilet', '2023-03-10 08:08:16'),
(22, '12', 'unknown', 'normal', 'Lack of toilet paper', '2023-03-10 08:15:06'),
(23, '', 'unknown', 'normal', 'Opis problemu / Description of problem / ', '2023-03-10 08:16:19'),
(24, '', 'unknown', 'medium', 'Opis problemu / Description of problem / ', '2023-03-10 08:18:28'),
(25, '', 'unknown', 'normal', 'Opis problemu / Description of problem / ', '2023-03-10 08:20:12'),
(26, '', 'unknown', 'normal', 'Opis problemu / Description of problem / ', '2023-03-10 08:21:00'),
(27, '', 'unknown', 'normal', 'Opis problemu / Description of problem / ', '2023-03-10 08:21:36'),
(28, '', 'unknown', 'normal', 'Opis problemu / Description of problem / ', '2023-03-10 08:22:18'),
(29, '99', 'Robert Lev', 'medium', 'Krzyki za ścianą', '2023-03-11 11:03:10');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `notes`
--
ALTER TABLE `notes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `notes`
--
ALTER TABLE `notes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
