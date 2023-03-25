Opis aplikacji:
Aplikacja webowa napisana w Python przy pomocy modułów: flask, pymysql, flask_bootstrap, 
obsługująca zestawienie floty wymyślonej linii lotniczej AirPol w formie bazy danych.
Użytkownik niezalogowany na możliwość przegladu danych i wyszukiwania. Użytkownik zalogowany, który nie ma uprawnień admina ma uprawnienia do dokonywania zmian w bazie danych. Użytkownik zalogowany, posiadający uprawnienia admina, może co poprzednik oraz dodawać, modyfikować i usuwać użytkowników. 


Aby uruchomić aplikację należy:
- baza danych została utworzona w MySQL, na serwerze PHPAdmin
- utworzyć bazę danych o nazwie aircraft2 i plik z bazą danych aircraft2.sql zaimportować do PHPAdmin
- ewentualnie dokonać korekt parametrów w liniach kodu wg wlasnych ustawień: con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2")
- w utworzyć folder dla aplikacji, do niego skopiować plik app.py
- w nim utworzyć podfolder Templates, do którego należy skopiować pliki html 
- w ide terminalu Pythona zainicjować środowisko wirtulane
- zainstalować moduły flask, flask_bootstrap, pymysql
- uruchomić w terminalu komendą flask run. 
 
