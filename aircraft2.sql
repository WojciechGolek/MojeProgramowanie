-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 25 Mar 2023, 15:30
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
-- Baza danych: `aircraft2`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `fleet`
--

CREATE TABLE `fleet` (
  `id` int(11) NOT NULL,
  `model` varchar(30) NOT NULL,
  `type` varchar(10) NOT NULL,
  `reg` varchar(10) NOT NULL,
  `year` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

--
-- Zrzut danych tabeli `fleet`
--

INSERT INTO `fleet` (`id`, `model`, `type`, `reg`, `year`) VALUES
(3, 'Boeing 777', 'B773', 'SQ-PLC', '2021'),
(5, 'Boeing 777', 'B773', 'SQ-PLE', '2019'),
(6, 'Airbus 319', 'A319', 'SQ-PLB', '2019'),
(7, 'Airbus 319', 'A320', 'SQ-PLF', '2019'),
(8, 'Airbus 320', 'A320', 'SQ-PLG', '2022'),
(9, 'Airbus 320', 'A320', 'SQ-PLH', '2013'),
(10, 'Boeing 787', 'B789', 'SQ-PLI', '2021'),
(11, 'Boeing 787', 'B788', 'SQ-PLJ', '2017'),
(12, 'Boeing 787', 'B788', 'SQ-PLK', '2020'),
(13, 'Boeing 787', 'B788', 'SQ-PLL', '2016'),
(18, 'Airbus 380', 'A388', 'SQ-PLO', '2018'),
(19, 'Boeing 777', 'B773', 'SQ-PLP', '2015'),
(20, 'Airbus 321', 'B21', 'SQ-PLP', '2009'),
(21, 'Boeing 777', 'B772', 'SQ-PLR', '2021'),
(22, 'Boeing 777', 'B772', 'SQ-PLR', '2021'),
(23, 'Airbus 380', 'A389', 'SQ-PLQ', '2014'),
(24, 'Embraer  195', 'E195LR', 'SQ-PLS', '2017'),
(25, 'Boeing 737MAX', 'B38M', 'SQ-PLT', '2022'),
(26, 'Airbus A330', 'A332', 'SQ-PLU', '2019'),
(27, 'Airbus A330', 'A333', 'SQ-PLV', '2013');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` text NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `is_active`, `is_admin`) VALUES
(8, 'mw', 'example@w.com', '0846fabe91ad87c3b6bc7cd7af2b3db43d916aa5f2374d5252b7154bb1dc362a', 1, 1),
(10, 'Wojt2', 'dwe@eerer.po', '89aba89cceb9cfd56dbd4bb8357c78c6599b5959d45bd54779d24fa61232498e', 1, 0),
(11, 'Pola', 'wew@reww.po', 'f26ee0a76888a0a0d4b74eae86ed94971e41c34a340ef5c8aa5d60cd37628823', 1, 0),
(12, 'Doda', 'fede@goor.ko', '2ad69c745421ee8e0e9f54f3246be2836e08138b266debe81d1072bb0f9c382a', 1, 0),
(13, 'jyug', 'sdfs', '2dd05ddb26fdda777835a4a6b1ae13b17644f740732b65629abba61abe4df36e', 1, 0);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `fleet`
--
ALTER TABLE `fleet`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `fleet`
--
ALTER TABLE `fleet`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT dla tabeli `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
