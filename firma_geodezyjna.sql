-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 09 Mar 2023, 10:54
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
-- Baza danych: `firma_geodezyjna`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pracownicy`
--

CREATE TABLE `pracownicy` (
  `id_pracownika` int(11) NOT NULL,
  `imie` varchar(15) COLLATE utf8_polish_ci NOT NULL,
  `nazwisko` varchar(15) COLLATE utf8_polish_ci NOT NULL,
  `zakres_uprawnień` varchar(5) COLLATE utf8_polish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `pracownicy`
--

INSERT INTO `pracownicy` (`id_pracownika`, `imie`, `nazwisko`, `zakres_uprawnień`) VALUES
(1, 'Marek', 'Król', '1'),
(2, 'Marcin', 'Arel', 'null'),
(3, 'Anna', 'Mikra', '2'),
(4, 'Grzegorz', 'Fiks', '1,2'),
(5, 'Damian', 'Golk', 'null'),
(6, 'Henryk', 'Polk', 'null'),
(7, 'Bożena', 'Markowska', '1'),
(8, 'Tomasz', 'Gryjas', 'null'),
(9, 'Sebastian', 'Mitręga', '1');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `przebieg_roboty`
--

CREATE TABLE `przebieg_roboty` (
  `id_roboty` int(10) UNSIGNED NOT NULL,
  `id_zleceniodawcy` int(11) NOT NULL,
  `data_rozpoczecia` date NOT NULL,
  `status` varchar(15) COLLATE utf8_polish_ci NOT NULL,
  `data_zakonczenia` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `przebieg_roboty`
--

INSERT INTO `przebieg_roboty` (`id_roboty`, `id_zleceniodawcy`, `data_rozpoczecia`, `status`, `data_zakonczenia`) VALUES
(1, 1, '2023-01-03', 'zakończona', '2023-02-01'),
(2, 2, '2023-01-09', 'trwa', '0000-00-00'),
(3, 3, '2023-01-13', 'trwa', '0000-00-00'),
(4, 5, '2023-01-16', 'zawieszona', '0000-00-00'),
(5, 1, '2023-01-16', 'zakończona', '2023-01-24'),
(6, 4, '2023-01-17', 'trwa', '0000-00-00'),
(7, 3, '2023-01-18', 'zakończona', '2023-01-31'),
(8, 2, '2023-01-19', 'trwa', '0000-00-00'),
(9, 1, '2023-01-20', 'trwa', '0000-00-00'),
(10, 3, '2023-01-24', 'zakończona', '2023-02-03'),
(11, 7, '2023-01-25', 'zakończona', '2023-02-03'),
(12, 6, '2023-01-26', 'trwa', '0000-00-00'),
(13, 8, '2023-01-27', 'trwa', '0000-00-00'),
(14, 3, '2023-01-27', 'zakończona', '2023-02-05'),
(15, 3, '2023-01-27', 'zakończona', '2023-02-07'),
(16, 1, '2023-01-29', 'trwa', '0000-00-00'),
(17, 6, '2023-01-30', 'zakończona', '2023-02-09'),
(18, 1, '2023-02-01', 'trwa', '0000-00-00'),
(18, 6, '2023-02-01', 'trwa', '0000-00-00');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `roboty_geodezyjne`
--

CREATE TABLE `roboty_geodezyjne` (
  `id_roboty` int(10) UNSIGNED NOT NULL,
  `numer_zlecenia` varchar(9) COLLATE utf8_polish_ci NOT NULL,
  `PODiG` varchar(20) COLLATE utf8_polish_ci NOT NULL DEFAULT 'Żywiec',
  `KERG_roboty` varchar(20) COLLATE utf8_polish_ci DEFAULT NULL,
  `obręb` varchar(15) COLLATE utf8_polish_ci NOT NULL,
  `asortyment` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `zakres_działki` varchar(50) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `roboty_geodezyjne`
--

INSERT INTO `roboty_geodezyjne` (`id_roboty`, `numer_zlecenia`, `PODiG`, `KERG_roboty`, `obręb`, `asortyment`, `zakres_działki`) VALUES
(1, '1/2023', 'Żywiec', 'GKNI.6640.25.2023', 'Nieledwia', 'mapa do celów projektowych', '254,236,237'),
(2, '2/2023', 'Żywiec', 'GKNI.6640.99.2023', 'Sól', 'podział działek', '25,26'),
(3, '3/2023', 'Żywiec', 'GKNI.6640.125.2023', 'Żywiec', 'wyznaczenie punktów  granicz', '587'),
(4, '4/2023', 'Cieszyn', 'GKNIC.6640.102.2023', 'Pruchna', 'mapa do celów projektowych', '11254,11365 oświetle'),
(5, '5/2023', 'Bielsko-Biała', 'GKNIBB.6640.250.2023', 'Lipnik', 'mapa do celów projektowych', '568,256 pod kanalizację'),
(6, '6/2023', 'Bielsko-Biała', 'GKNIBB.6640.259.2023', 'Lipnik', 'mapa do celów projektowych', '1022,1023/2 pod kanalizację'),
(7, '7/2023', 'Cieszyn', 'GKNIC.6640.192.2023', 'Cieszyn', 'mapa do celów projektowych', '568'),
(8, '8/2023', 'Żywiec', 'GKNI.6640.333.2023', 'Zwardoń', 'podział działki', '12351'),
(9, '9/2023', 'Żywiec', 'GKNI.6640.255.2023', 'Pewel', 'inwentaryzacja budynku', '54/5'),
(10, '10/2023', 'Żywiec', 'GKNI.6640.255.2023', 'Korbielów', 'inwentaryzacja budynku', '254,236'),
(11, '11/2023', 'Cieszyn', 'GKNIC.6640.255.2023', 'Cieszyn', 'mapa do celów projektowych', '1254/8'),
(12, '12/2023', 'Bielsko-Biała', 'GKNIBB.6640.426.2023', 'Mikuszowice', 'mapa do celów projektowych', '548'),
(13, '13/2023', 'Żywiec', 'GKNI.6640.487.2023', 'Żywiec', 'wyznaczenie punktów  granicz', '2587,3000/3'),
(14, '14/2023', 'Żywiec', 'GKNI.6640.622.2023', 'Pewel', 'podział działki', '788'),
(15, '15/2023', 'Żywiec', 'GKNI.6640.985.2023', 'Zwardoń', 'mapa do celów projektowych', '425,426,427/2'),
(16, '16/2023', 'Żywiec', 'GKNI.6640.1124.2023', 'Żywiec', 'wyznaczenie punktów  granicz', '468,469/2'),
(17, '17/2023', 'Żywiec', 'GKNI.6640.1255.2023', 'Nieledwia', 'mapa do celów projektowych', '587'),
(18, '18/2023', 'Żywiec', 'GKNI.6640.1455.2023', 'Nieledwia, Sól', 'mapa do celów projektowych', 'oświetlenie dwóch gmin, droga przelotowa');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zespol_roboczy`
--

CREATE TABLE `zespol_roboczy` (
  `id_roboty` int(10) UNSIGNED NOT NULL,
  `id_pracownika` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `zespol_roboczy`
--

INSERT INTO `zespol_roboczy` (`id_roboty`, `id_pracownika`) VALUES
(1, 3),
(1, 5),
(2, 1),
(2, 8),
(3, 7),
(3, 8),
(3, 9),
(4, 5),
(4, 2),
(5, 6),
(5, 1),
(5, 4),
(6, 2),
(7, 7),
(7, 1),
(8, 9),
(8, 2),
(9, 2),
(9, 3),
(10, 3),
(11, 4),
(11, 6),
(12, 2),
(12, 4),
(13, 6),
(13, 8),
(14, 1),
(14, 6),
(14, 5),
(15, 6),
(15, 8),
(16, 3),
(16, 4),
(16, 7),
(17, 3),
(17, 9),
(17, 6),
(18, 6),
(18, 7),
(18, 8);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zleceniodawca`
--

CREATE TABLE `zleceniodawca` (
  `id_zleceniodawcy` int(11) NOT NULL,
  `nazwa_imie_nazwisko` varchar(30) COLLATE utf8_polish_ci NOT NULL,
  `NIP` int(10) DEFAULT NULL,
  `ulica_nr_domu` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  `miasto` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  `kod` varchar(6) COLLATE utf8_polish_ci NOT NULL,
  `kontakt` varchar(30) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `zleceniodawca`
--

INSERT INTO `zleceniodawca` (`id_zleceniodawcy`, `nazwa_imie_nazwisko`, `NIP`, `ulica_nr_domu`, `miasto`, `kod`, `kontakt`) VALUES
(1, 'Urząd Gminy Wotlin', 65987521, 'Główna 25', 'Wotlin', '56-985', '552985478'),
(2, 'Marian Glac', 0, 'Polna 56', 'Drebsko', '36-587', '321654652'),
(3, 'Mediax Sp. z o.o.', 58745874, 'Mała 25B', 'Dryksy', '85-587', 'kontakt2@mediax,pl'),
(4, 'Halina Płaza', 0, 'Do Pola 13', 'Nowa Wieś', '86-787', '152365125'),
(5, 'Michał Golasik', 0, 'Klocka 125', 'Babiniec', '65-698', '5695425'),
(6, 'Urząd Gminy Świerc', 985658745, 'Świerc 2', 'Świerc', '88-695', '213265454'),
(7, 'Anna Dok', 0, 'Majowa 25C', 'Wolsko', '56-898', '496587457'),
(8, 'Bolesław Birkut', 0, 'Wąska 54', 'Sieńsk', '23-987', 'bbir@dwes.com.pl');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `pracownicy`
--
ALTER TABLE `pracownicy`
  ADD PRIMARY KEY (`id_pracownika`);

--
-- Indeksy dla tabeli `przebieg_roboty`
--
ALTER TABLE `przebieg_roboty`
  ADD KEY `id_zleceniodawcy` (`id_zleceniodawcy`),
  ADD KEY `id_roboty` (`id_roboty`);

--
-- Indeksy dla tabeli `roboty_geodezyjne`
--
ALTER TABLE `roboty_geodezyjne`
  ADD PRIMARY KEY (`id_roboty`);

--
-- Indeksy dla tabeli `zespol_roboczy`
--
ALTER TABLE `zespol_roboczy`
  ADD KEY `id_roboty` (`id_roboty`),
  ADD KEY `id_pracownika` (`id_pracownika`);

--
-- Indeksy dla tabeli `zleceniodawca`
--
ALTER TABLE `zleceniodawca`
  ADD PRIMARY KEY (`id_zleceniodawcy`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `pracownicy`
--
ALTER TABLE `pracownicy`
  MODIFY `id_pracownika` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT dla tabeli `roboty_geodezyjne`
--
ALTER TABLE `roboty_geodezyjne`
  MODIFY `id_roboty` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT dla tabeli `zleceniodawca`
--
ALTER TABLE `zleceniodawca`
  MODIFY `id_zleceniodawcy` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `przebieg_roboty`
--
ALTER TABLE `przebieg_roboty`
  ADD CONSTRAINT `przebieg_roboty_ibfk_1` FOREIGN KEY (`id_zleceniodawcy`) REFERENCES `zleceniodawca` (`id_zleceniodawcy`),
  ADD CONSTRAINT `przebieg_roboty_ibfk_2` FOREIGN KEY (`id_roboty`) REFERENCES `roboty_geodezyjne` (`id_roboty`);

--
-- Ograniczenia dla tabeli `zespol_roboczy`
--
ALTER TABLE `zespol_roboczy`
  ADD CONSTRAINT `zespol_roboczy_ibfk_1` FOREIGN KEY (`id_roboty`) REFERENCES `roboty_geodezyjne` (`id_roboty`),
  ADD CONSTRAINT `zespol_roboczy_ibfk_2` FOREIGN KEY (`id_pracownika`) REFERENCES `pracownicy` (`id_pracownika`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
