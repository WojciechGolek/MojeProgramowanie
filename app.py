from flask import Flask, render_template, url_for, request, flash, redirect
from flask import session # do sesji logowania i przechowania informacji o sesji w formie słownika
from flask_bootstrap import Bootstrap
import pymysql as mysql 
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "sekretne"

allMatches = []
l = None

"""wykorzystany kod zagadnienia Round-robin_tournament, czyli wygenerowania kolejek ligowych 
czyli meczów po  2 na pare zespołów, i dodatkowo podzielenia tych meczów na kolejki ligowe,
czyli każdy zespół gra raz w kolejce"""
def matches (teams):
    if len(teams) % 2:
        teams.append('Bez meczu')
    n = len(teams)
    matchs = []
    fixtures = []
    return_matchs = []
    for fixture in range(1, n):
        for i in range(int(n/2)):
            matchs.append((teams[i], teams[n - 1 - i]))
            return_matchs.append((teams[n - 1 - i], teams[i]))
        teams.insert(1, teams.pop())
        fixtures.insert(1, matchs)
        fixtures.append(return_matchs)
        matchs = []
        return_matchs = []

    return fixtures  # zwraca listy - kolejki ligowe, w listach tuple jako pary meczowe

"""konieczne istnienie bazych danych football_league zawierającej dwie tabele:
1/ standings  z kolumnami `id`, `team`, `matches`, `points`, `goals_scored`, `goals_lost`, `won`, `draw`, `lost`
2/ matches `id`, `teamA`, `teamB`, `goalA`, `goalB`
metoda czyści bazę  z danych i zeruje wartosci
połączenie z baza danych poprzez moduł pymysql
"""
def initBase (teams, allMatches):
    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="football_league")
    cur = con.cursor()
    sqlQuery = "TRUNCATE TABLE standings"
    cur.execute(sqlQuery)
    sqlQuery = "TRUNCATE TABLE matches"
    cur.execute(sqlQuery)
    con.commit ()
    for team in teams:
        sqlQuery = "INSERT INTO `standings` (`id`, `team`, `matches`, `points`, `goals_scored`, `goals_lost`, `won`, `draw`, `lost`) VALUES (NULL, %s, '0', '0', '0', '0', '0', '0', '0');"
        cur.execute(sqlQuery, [team])
        con.commit ()
    for match in allMatches:
        for i in range (0,l):
            sqlQuery = "INSERT INTO `matches` (`id`, `teamA`, `teamB`, `goalA`, `goalB`) VALUES (NULL, %s, %s, Null, Null);"
            cur.execute(sqlQuery,  [match[i][0], match[i][1] ] )
            con.commit ()
    print ('initbase', allMatches, 'initbase')

"""funkcja do startu aplikcji i podaniu zespołów w rozgrywkach w pliku txt
funkcja wczytuje plik, przekazuje go metody matches """
@app.route("/start", methods = ["GET", "POST"]) 
def start():
     if request.method == "GET": 
        return render_template("start.html")
     if request.method == "POST":
        scriptDir = os.path.dirname (__file__) # katalog w którym jest wykonywany plik aplikacji
        print (scriptDir)  
        if not os.path.exists (scriptDir + "/teams.txt"):
            flash ('brak pliku')    
            return render_template("start.html")  
        else:
            with open (scriptDir + "/teams.txt", "r", encoding= "utf-8") as fh:
                teams = fh.readlines ()
                fh.close ()
            numberOfTeams = len (teams)
            global allMatches
            allMatches = matches(teams)
            global l
            l = len(allMatches[0])
            initBase (teams, allMatches)
            return render_template("start_plus.html", enumerate=enumerate, teams=teams, allMatches=allMatches, l = l, numberOfTeams=numberOfTeams)

"""metoda wyświetlająca aktualną tabelę rozgrywek, o kolelności decydują punkty, gole strzelone, 
gole stracone"""
@app.route("/tabela", methods = ["GET"]) 
def tabela():
    if request.method == "GET":
        con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="football_league")
        cur = con.cursor()
        sqlQuery = "SELECT ROW_NUMBER() OVER( ORDER BY points DESC, goals_scored DESC, goals_lost) as miejsce, team, matches, points, goals_scored, goals_lost, won, draw, lost FROM standings"
        cur.execute(sqlQuery)
        databaseList = cur.fetchall()
        sqlQuery = f"SELECT teamA, goalA, goalB, teamB FROM matches;"
        cur.execute(sqlQuery)
        allGames = cur.fetchall()
        cur.close()
        print (allGames)
    return render_template ("tabela.html", databaseList=databaseList, enumerate=enumerate, allMatches=allMatches, l = l, allGames=allGames)

"""Metoda wyświetlające wszystkie mecze w kolejkach ligowych na podstawie wykonania metody matches
przy meczach tworzony jest formularz do przesłania wyniku meczu.
Jeśli wyniik nie istnieje w tabeli matches, jest on do niej dodawany oraz wykonywana jest logika
dla zaktualizowania danych w bazie danych tabeli standings, a w konsekwencji wygenerowania
aktualnej  tabeli ligowej na stronie tabela.html
 """
@app.route("/mecze", methods = ["GET", "POST"]) 
def mecze ():
    if request.method == "GET":
        scriptDir = os.path.dirname (__file__) # katalog w którym jest wykonywany plik
        print (scriptDir)  
        if not os.path.exists (scriptDir + "/teams.txt"):
            flash ('brak pliku')    
            return render_template("start.html")  
        else:
            with open (scriptDir + "/teams.txt", "r", encoding= "utf-8") as fh:
                teams = fh.readlines ()
                fh.close ()
            numberOfTeams = len (teams)
            allMatches = matches(teams)
        l = len(allMatches[0])
        return render_template ("mecze.html", allMatches=allMatches, enumerate=enumerate, l = l)
                            
    if request.method == "POST":
        if "A" in request.form:
            A = request.form["A"] 
        if "B" in request.form: 
            B = request.form["B"]
        if "goalA" in request.form: 
            goalA = int (request.form["goalA"])
        if "goalB" in request.form: 
            goalB = int (request.form["goalB"])
        
        con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="football_league")
        cur = con.cursor()
        sqlQuery = f"SELECT * FROM `matches` WHERE teamA LIKE '%{A}%' and teamB like '%{B}%';"
        cur.execute(sqlQuery)
        match = cur.fetchone()
        print ("wpis wyniku", match, "wpis wyniku")
        if match [3] != None or match [4] != None:
            flash ("Result of game already exists in database -->  ")
            flash (f" {match[1]} {match[3]} : {match[4]} {match[2]}" )
            con.close()
            return redirect(url_for("mecze") )
            
        else:
            sqlQuery = f"UPDATE `matches` SET `goalA` = {goalA}, `goalB` = {goalB} WHERE teamA LIKE '%{A}%' and teamB like '%{B}%';"
            cur.execute(sqlQuery)
            con.commit()    

            sqlQuery = f"SELECT * FROM `standings` WHERE team like '%{A}%'"
            cur.execute(sqlQuery)
            teamA = cur.fetchone()
            sqlQuery = f"SELECT * FROM `standings` WHERE team like '%{B}%'"
            cur.execute(sqlQuery)
            teamB = cur.fetchone()

            if goalA > goalB:
                sqlQuery = "UPDATE `standings` SET `matches` = %s, `points` = %s, `goals_scored` = %s, `goals_lost` = %s, `won` = %s WHERE `standings`.`team` like %s" 
                cur.execute(sqlQuery, [teamA[2]+1, teamA[3]+3, teamA[4]+goalA, teamA[5]+goalB, teamA[6]+1, teamA[1]])
                con.commit()
                
                sqlQuery2 = "UPDATE `standings` SET `matches` = %s, `points` = %s, `goals_scored` = %s, `goals_lost` = %s, `lost` = %s WHERE `standings`.`team` like %s" 
                cur.execute(sqlQuery2, [teamB[2]+1, teamB[3], teamB[4]+goalB, teamB[5]+goalA, teamB[8]+1, teamB[1]])
                con.commit()
                
            if goalA < goalB:
                sqlQuery = "UPDATE `standings` SET `matches` = %s, `points` = %s, `goals_scored` = %s, `goals_lost` = %s, `lost` = %s WHERE `standings`.`team` like %s" 
                cur.execute(sqlQuery, [teamA[2]+1, teamA[3], teamA[4]+goalA, teamA[5]+goalB, teamA[8]+1, teamA[1]])
                con.commit()
                
                sqlQuery2 = "UPDATE `standings` SET `matches` = %s, `points` = %s, `goals_scored` = %s, `goals_lost` = %s, `won` = %s WHERE `standings`.`team` like %s" 
                cur.execute(sqlQuery2, [teamB[2]+1, teamB[3]+3, teamB[4]+goalB, teamB[5]+goalA, teamB[6]+1, teamB[1]])
                con.commit()
            
            if goalA == goalB:
                sqlQuery = "UPDATE `standings` SET `matches` = %s, `points` = %s, `goals_scored` = %s, `goals_lost` = %s, `draw` = %s WHERE `standings`.`team` like %s" 
                cur.execute(sqlQuery, [teamA[2]+1, teamA[3]+1, teamA[4]+goalA, teamA[5]+goalB, teamA[7]+1, teamA[1]])
                con.commit()
                
                sqlQuery2 = "UPDATE `standings` SET `matches` = %s, `points` = %s, `goals_scored` = %s, `goals_lost` = %s, `draw` = %s WHERE `standings`.`team` like %s" 
                cur.execute(sqlQuery2, [teamB[2]+1, teamB[3]+1, teamB[4]+goalB, teamB[5]+goalA, teamB[7]+1, teamB[1]])
                con.commit()
                con.close()
            return redirect(url_for("tabela") )
            


            
            
        
                                
