Baza danych wykonana w MySQL - phpMyAdmin.
Projekt bazy danych do zarządzania firmą geodezyjną. W takiej firmie pracownicy pogrupowani w róznej konfiguracji mniejsze zespoły są przydzielani do wykonynywania poszczególnych zleceń.
Tabele wypełniono fikcyjnymi danymi.
Tabele:
- pracownicy ( klucz podstawowy id_pracownika),
- zespol_roboczy (klucze obce: id_pracownika, id_roboty) 
- roboty_geodezyjne (klucz podstawowy: id_roboty)
- przebieg_roboty (klucze obce: id_roboty, id_zleceniodawcy)
- zleceniodawca (klucz podstawowy: id_zleceniodawcy)
