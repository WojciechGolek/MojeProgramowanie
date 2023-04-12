Opis aplikacji:
Aplikacja webowa napisana w Python przy pomocy modułów: flask, pymysql, flask_bootstrap, 
obsługująca rozgrywki ligowe w dowolnej dyscyplinie drużynowej, przy czym tutaj założono rozgrwyki piłki nożnej.
Z pliku teams.txt wczytywane są zespoły, jest tworzona daza meczów całego sezonu w systemie mecz-rewanż i generowana jest tabela ligowa. O kolejlności decydują punkty, gole strzelone i 
gole stracone. Uzytkownik na możliwość wprowadzania danych, tj. wyników meczów. Dane są przechowywane w bazie danych, w jednej tabeli dane po rozegranych meczach poszczególnych zespołów, w drugiej mecze z wynikami.


Aby uruchomić aplikację należy:
- mieć zainstalowany pakiet XAMPP 
- w środowisku PHP Admin utworzyć bazę danych i do niej zaimportowac plik z bazą football_league.sql   
baza w strukturze dwóch tabel:
1/ standings  `id`, `team`, `matches`, `points`, `goals_scored`, `goals_lost`, `won`, `draw`, `lost`
2/ matches `id`, `teamA`, `teamB`, `goalA`, `goalB`
- w folderze aplikacji przygotowac plik teams.txt z drużynami w osobnych liniach,w przypadku nieparzystej liczby drużyn dodaje sie "wolny los"
- ewentualnie dokonać korekt parametrów w liniach kodu wg wlasnych ustawień: con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") plus secret_key
- utworzyć folder dla aplikacji, do niego skopiować pliki i foldery
- w ide terminalu Pythona zainicjować środowisko wirtulane
- zainstalować moduły flask, flask_bootstrap, pymysql
- uruchomić w terminalu komendą flask run. 
 
