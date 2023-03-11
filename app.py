"""Aplikacja do zgłaszania usterek przez gości hotelowych
Napisana z użyciem biblioteki Flask oraz pymysql
Wygląd stron został zapisany w plikach html, dołączanych jako szablony Jinja """

from flask import Flask, render_template, url_for, request, flash
import datetime
import time
import pymysql as mysql 

app = Flask(__name__)
app.config["SECRET_KEY"] = "sekretne"

#utworzenie klas dla zainicjowania poziomu ważnosci zgłoszeń
class PriorityType:
    def __init__ (self,code, description):
        self.code = code
        self.description = description

# zainicjowanie listy i wypełnienie jej obiektami klasy PriorityType
class NotificationPriorities:
    def __init__ (self):
        self.listOfPriorities = []
    
    def loadPriorities (self): 
        self.listOfPriorities.append (PriorityType ("normal","Normalna / normal") )
        self.listOfPriorities.append (PriorityType ("medium","Średnia / Medium") )
        self.listOfPriorities.append (PriorityType ("high","Wysoka / High") )
    
    # metoda do iteracji i wczytania kodu złoszenia 
    def getPriorityByCode (self, code): 
        for el in self.listOfPriorities:
            if el.code == code:
                return el
    
# metoda wyświatylająca formularz
@app.route("/notification", methods=["GET", "POST"])
def notification():
    notificationPriorities = NotificationPriorities()
    notificationPriorities.loadPriorities() #wypełnienie obiektu po wywolaniu metody loadPriorities.
    hourNow = datetime.datetime.now().hour
    noteTime = time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime() )

    if request.method == "GET": # po prostu pierwsze wyświetylenie strony
        
        return render_template("formularz.html",listOfPriorities=notificationPriorities.listOfPriorities)
    else: # jeśli metoda "POST" czyli po wysłaniu formularza
        
        if "roomNumber" in request.form: # jeśli użytkownik przesłał do nas pole o nazwie roomNumber
            roomNumber = request.form["roomNumber"] 

        if "name" in request.form: 
            name = request.form["name"]

        if "nazwa" in request.form: 
            nazwa = request.form["nazwa"]

        if "priority" in request.form: 
            priority = request.form["priority"]
        
        flash("Notification has been sent to hotel")

        # w ptrzypadku zgłoszeń z priorotetem medium w porze nocnej, priority wzrasta na high
        if priority == "medium" and (hourNow > 20 and hourNow <6):
            priority = "high"
            flash("Rising priority from medium to high")
            
        try: 
            # połączenie z bazą danych utworzoną w PHPMy Admin  
            con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="room") 	
            cur = con.cursor()
            # zapisanie wpisu do bazy
            query1 = "INSERT INTO `notes` (`id`, `roomNumber`, `guestName`, `priority`, `description`, `timestamp`) VALUES (%s, %s, %s, %s, %s, %s)"
            cur.execute(query1, ['NULL', roomNumber, name, priority, nazwa, noteTime])
            con.commit()
            cur.close()
        except mysql.err.OperationalError as error:
            # wyłapanie wyjątku błędu połączenia z bazą
            print (f"Błąd połączenia:  {error}\n Dane nie zapisane do bazy")
        
        priority = notificationPriorities.getPriorityByCode(priority)
        # wczytanie parametru priority z listy poprzez metodę getPriorityByCode
        return render_template ("formularz_content.html", roomNumber=roomNumber, nazwa=nazwa,name=name,
                                priority=priority, hourNow=hourNow) 
        # wczytanie szablonu strony z podsumowaniem   



