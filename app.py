
from flask import Flask, render_template, url_for, request, flash, redirect
from flask import session # do sesji logowania i przechowania informacji o sesji w formie słownika
from flask_bootstrap import Bootstrap
import pymysql as mysql 
import random 
import string 
import hashlib # do wyliczania hasha hasła
import binascii # zamiana wartosci binarnych w kod ascii

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "sekretne"

"""klasa UserPass przechowuje dane użytkownika"""
class UserPass: 
    def __init__(self, user='', password=''):
        self.user = user
        self.password = password
        self.email = '' 
        self.is_valid = False # do przechowania info czy konto aktywne, wypelnione
        self.is_admin = False # czy ten user jest adminem
    
    """funkcja do zahaszowania hasła użytkownika"""
    def hash_password (self):
        # salt_random = os.urandom(10) do wygenerowania salt
        salt = b"b\x9a\xec.@\r\x0c\x1c\xbc,+"
        passwordHash = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), salt, 100000)
        passwordHash = binascii.hexlify(passwordHash)
        return passwordHash

    """funkcja porównująca przechowane zahaszowane hasło z wprowadzonym przy logowaniu"""
    def verify_password(self, stored_password, provided_password):
        salt = b"b\x9a\xec.@\r\x0c\x1c\xbc,+"
        passwordHash2 = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
        passwordHash2 = binascii.hexlify(passwordHash2)
        print ("provided_zahasz", passwordHash2)
        return passwordHash2 == bytes (stored_password, 'utf-8') 
    
    """funkcja przy inicjacji aplikacji do stworzenie losowego uzytkownika (admina) i jego hasla"""
    def get_random_user_pasword(self):  
        random_user = ''.join(random.choice(string.ascii_lowercase)for i in range(5)) 
        self.user = random_user 
        password_characters = string.ascii_letters + string.digits
        random_password = ''.join(random.choice(password_characters)for i in range(5)) 
        self.password = random_password
        print (random_password, 'password wylosowane')
    
    """ funkcja  czy użytkownik jest w bazie danych i czy wprowadzil dobre haslo"""
    def login_user(self):
        con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2")
        cur = con.cursor()
        sqlQuery = "SELECT id, name, email, password, is_active, is_admin FROM `users` WHERE name=%s"
        cur.execute(sqlQuery, [self.user])
        user_record = cur.fetchone()

        if user_record !=None and self.verify_password(user_record[3], self.password):
            return user_record
        else:
            self.user = None
            self.password = None
            return None
    
    def get_user_info (self):
        con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2")
        cur = con.cursor()
        sqlQuery = "SELECT name, email, is_active, is_admin FROM `users` WHERE name=%s"
        cur.execute(sqlQuery, [self.user])
        db_user = cur.fetchone()

        if db_user == None:
            self.is_valid = False
            self.is_admin = False
            self.email = ''
        elif db_user[2] != 1:
            self.is_valid = False
            self.is_admin = False
            self.email = db_user[1] # tuple
        else:
            self.is_valid = True
            self.is_admin = db_user[3]
            self.email = db_user [1]


"""funkcja do starru aplikcji przy 1 razie np. po instalacji"""
@app.route("/init_app") 
def init_app():
    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2")
    cur = con.cursor()
    sqlQuery = "SELECT COUNT(*) as cnt FROM `users` WHERE is_active and is_admin"
    cur.execute(sqlQuery)
    active_admins = cur.fetchone()

    if active_admins[0]>0:
        flash ("Aplication is already set-up. Nothing to do.")
        return redirect(url_for('index'))
    
    # jeśli nie ma admina tworzymy/updatujemy go z kontem i haslem
    user_pass = UserPass() 
    user_pass.get_random_user_pasword()
    sqlQuery = "INSERT INTO `users` (`name`, `email`, `password`, `is_active`, `is_admin`) VALUES (%s, %s, %s, %s, %s);"
    cur.execute(sqlQuery,[user_pass.user, "example@w.com",user_pass.hash_password(), True,True])
    con.commit()
    flash ("User {}  with password {} has been created".format (user_pass.user, user_pass.password))
    return redirect (url_for ("index"))

"""funkcja logowania"""
@app.route("/login", methods = ["GET", "POST"])
def login ():
    login = UserPass (session.get('user') ) # tworzy obiekt dla uzytkownika ktory moze byc teraz w sesji
    login.get_user_info() 

    if request.method == "GET":
        return render_template("login.html", active_menu="login", login=login)
        # login informacja o tym jaki uzytkownik teraz pracuje
    else:
        if "user_name" not in request.form:
            user_name = ""
        else: 
            user_name = request.form["user_name"]

        if "user_pass" not in request.form:
            user_pass = ""
        else: 
            user_pass = request.form["user_pass"]
        
        login = UserPass (user_name, user_pass)
        login_record = login.login_user()

        if login_record !=None:
            session["user"] = user_name 
            """ session sa trzymane w słowniku, dlatego tu przypisanie do klucza user wartosci user_name"""
            flash ("Logon succesfull, welcome {}".format(user_name))
            return redirect (url_for("index"))
        else:
            flash("Logon failed, try again")
            return render_template("login.html", login=login, active_menu = 'login')

@app.route("/logout")
def logout():

    if "user" in session:
        session.pop("user", None) #drugi parametr jest zwracany, jeśli brak pierwszego klucza
        flash ("You are logged out")
    return redirect(url_for("index"))

"""główna strona bazy danych, wyświetlana jest flota """
@app.route("/index", methods=["GET", "POST"])
def index():
    login = UserPass (session.get('user') ) # tworzy obiekt dla uzytkownika ktory moze byc teraz w sesji
    login.get_user_info() 
    try: 
        # połączenie z bazą danych utworzoną w PHPMy Admin  
        con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
        cur = con.cursor()
        sqlQuery = "SELECT id, model, type, reg, year FROM fleet"
        cur.execute(sqlQuery)
        databaseList = cur.fetchall()
        cur.close()
        listLen = len (databaseList)
    except mysql.err.OperationalError as error:
        # wyłapanie wyjątku błędu połączenia z bazą
        print (f"Błąd połączenia:  {error}\n Dane nie zapisane do bazy")
    return render_template ("index.html",databaseList=databaseList, listLen=listLen, login=login, active_menu='Main page') 

"""dodawanie nowego rekordu w bazie"""
@app.route("/add", methods=["GET", "POST"])
def add():
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if login.is_valid is False:
        return redirect (url_for('login'))#  odc. 40 implement""" 
    
    if request.method == "GET": # po prostu pierwsze wyświetylenie strony
        return render_template("add.html",login=login)
    else: # jeśli metoda "POST" czyli po wysłaniu formularza
        if "model" in request.form:
            model = request.form["model"] 
        if "type" in request.form: 
            type = request.form["type"]
        if "reg" in request.form: 
            reg = request.form["reg"]
        if "year" in request.form: 
            year = request.form["year"]
        try: 
            # połączenie z bazą danych utworzoną w PHPMy Admin  
            con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
            cur = con.cursor()
            sqlQuery1 = "INSERT INTO `fleet` (`id`, `model`, `type`, `reg`, `year`) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sqlQuery1, ['NULL', model, type, reg, year])
            con.commit()
            con.close()
            flash ("Dodano do bazy")
        except mysql.err.OperationalError as error:
            print (f"Błąd połączenia:  {error}\n Dane nie zapisane do bazy")

        return render_template ("add.html",login=login)

"""edycja rekordu bazy"""
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if login.is_valid is False:
        return redirect (url_for('login'))

    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
    cur = con.cursor()
    sqlQuery = "SELECT id, model, type, reg, year FROM fleet WHERE id = %s"
    cur.execute(sqlQuery, id)
    record = cur.fetchone()

    if request.method == "GET":
        return render_template ("edit.html", record=record, login=login)
    else: # jeśli metoda "POST" czyli po wysłaniu formularza
        if "model" in request.form:
            model = request.form["model"] 
        if "type" in request.form: 
            type = request.form["type"]
        if "reg" in request.form: 
            reg = request.form["reg"]
        if "year" in request.form: 
            year = request.form["year"]

        sqlQuery2 = "UPDATE `fleet` SET `model` = %s, `type`=%s, `reg` = %s, `year` = %s WHERE `fleet`.`id` = %s"
        cur.execute(sqlQuery2, [model, type, reg, year,id])
        con.commit()
        con.close()
        flash ("Item was changed")

        return redirect(url_for ('index'))

"""wyszukiwanie, wpisana fraza jest traktowana jako fragment łańcucha"""
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET": # po prostu pierwsze wyświetlenie strony
        return render_template("search.html")
    else:
        if "model" in request.form:
            model = request.form["model"] 
        if "type" in request.form:
            type = request.form["type"] 
        if "reg" in request.form:
            reg = request.form["reg"] 
        if "year" in request.form:
            year = request.form["year"] 

        try: 
            # połączenie z bazą danych utworzoną w PHPMy Admin  
            con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
            cur = con.cursor()
            sqlQuery2= f"SELECT * FROM `fleet` WHERE (model LIKE '%{model}%') and (type LIKE '%{type}%') and (reg LIKE '%{reg}%') and (year LIKE '%{year}%')  "
            cur.execute(sqlQuery2)
            databaseList1 = cur.fetchall()
            cur.close()
            listLen = len (databaseList1)
        
        except mysql.err.OperationalError as error:
            print (f"Błąd połączenia:  {error}\n Dane nie zapisane do bazy")

        return render_template ("search_result.html", databaseList1=databaseList1, listLen=listLen)

@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if login.is_valid is False:
        return redirect (url_for('login'))#  odc. 40 implement"""
    try: 
        con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
        cur = con.cursor()
        sqlQuery2= f" DELETE FROM `fleet` WHERE `fleet`.`id` = %s  "
        cur.execute(sqlQuery2, [id])
        con.commit()
        cur.close()
        
    except mysql.err.OperationalError as error:
            print (f"Błąd połączenia:  {error}\n Dane nie zapisane do bazy")
    return redirect(url_for("index") )

"""wyświetlenie użytkowników, konieczne uprawnienia administratora, czyli is_admin == True"""
@app.route("/users")
def users ():
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if  login.is_valid == False or login.is_admin == False:
        flash ('Wymagane uprawnienia administratora')
        return redirect (url_for('login'))
    
    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
    cur = con.cursor()
    sqlQuery = "SELECT id, name, email, is_active, is_admin FROM `users`"
    cur.execute(sqlQuery)
    users = cur.fetchall()

    return render_template ('users.html', users=users, login=login)

"""funkcja pozwala zmienic pole is_active is_admin dla wybranego uzytkownika"""
@app.route ("/user_status_change/<action>/<user_name>")
def user_status_change (action, user_name):
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if  login.is_valid == False or login.is_admin == False:
        flash ('Wymagane uprawnienia administratora')
        return redirect (url_for('login'))
    
    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
    cur = con.cursor()
    if action == 'active':      # parametr z route
        sqlQuery = "UPDATE users SET is_active = (is_active + 1) MOD 2 WHERE name = %s and name <> %s"
        cur.execute(sqlQuery, [user_name, login])
        con.commit()

    elif action == 'admin': # parametr z route
        sqlQuery = "UPDATE users SET is_admin = (is_admin + 1) MOD 2 WHERE name = %s and name <> %s"
        # modulo musi jako MOD, a nie % !
        cur.execute(sqlQuery, [user_name, login])
        con.commit()
    
    return redirect (url_for ('users'))

"""edycja użytkownika """
@app.route ("/edit_user/<user_name>", methods=["GET", "POST"])
def edit_user (user_name):
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if  login.is_valid == False or login.is_admin == False:
        flash ('Wymagane uprawnienia administratora')
        return redirect (url_for('login'))
    
    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
    cur = con.cursor()
    sqlQuery = "SELECT name, email FROM `users` WHERE name = %s"
    cur.execute(sqlQuery, [user_name])
    user = cur.fetchone()
    message = None

    if user == None:
        flash ("No such user")
        return redirect (url_for ('users'))

    if request.method == "GET":
        return render_template('edit_user.html', user=user, login=login)
    else:
        new_email = "" if "email" not in request.form else request.form["email"]
        new_password = "" if "user_pass" not in request.form else request.form["user_pass"]

    if new_email != user[1]:
        sqlQuery = "UPDATE `users` SET email = %s WHERE name = %s"
        cur.execute(sqlQuery, [new_email, user_name])
        con.commit()
        flash ("Email was changed")

    if new_password != "":
        user_pass = UserPass (user_name, new_password)
        sqlQuery = "UPDATE `users` SET password = %s WHERE name = %s"
        cur.execute(sqlQuery, [new_password, user_name])
        con.commit()
        flash ("Password was changed")
    
    return redirect(url_for ('users'))

"""wykasowanie użytkownika"""
@app.route ("/delete_user/<user_name>") # tu przyjdzie parametr user_name z users.html
def delete_user (user_name):
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if  login.is_valid == False or login.is_admin == False:
        flash ('Wymagane uprawnienia administratora')
        return redirect (url_for('login'))
    
    login = session ['user'] # nazwa aktualnego użytkownika
    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
    cur = con.cursor()
    sqlQuery= " DELETE FROM `users` WHERE name = %s and name <> %s"
    # usuń usera o nazwie, ale który nie jest zalogowany obecnie
    cur.execute(sqlQuery, [user_name, login])
    con.commit()
    
    return redirect(url_for ('users'))

"""dodanie nowego użytkownika"""
@app.route ("/new_user",  methods=["GET", "POST"])
def new_user ():
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if login.is_valid is False:
        return redirect (url_for('login'))

    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2")
    cur = con.cursor()
    message = None
    user = {}

    if request.method == "GET":
        return render_template ("new_user.html", active_menu="users", user=user)
    else: # wypelnienie slownika user
        if not 'user_name' in request.form:
            user['user_name'] = '' 
        else:
            user['user_name'] = request.form ['user_name']

        if not 'email' in request.form:
            user['email'] = '' 
        else:
            user['email'] = request.form ['email']

        if not 'user_pass' in request.form:
         user['user_pass'] = ''  
        else:
            user['user_pass'] = request.form ['user_pass']

        #poniżej sprawdzenia przesyłanych danych, czy user jest bazie 
        sqlQuery = "SELECT COUNT(*) as cnt FROM `users` WHERE name = %s"
        cur.execute(sqlQuery, [user['user_name'] ] )
        record = cur.fetchone()
        is_user_name_unique = (record[0] == 0 ) # zwraca True lub False !

        sqlQuery = "SELECT COUNT(*) as cnt FROM `users` WHERE email = %s"
        cur.execute(sqlQuery, [user['email'] ] )
        record = cur.fetchone()
        is_user_email_unique = (record[0] == 0 )

        if user['user_name'] == '':
            message = "Name cannot be empty"
        elif user['email'] == '':
            message = "Email cannot be empty"
from flask import Flask, render_template, url_for, request, flash, redirect
from flask import session # do sesji logowania i przechowania informacji o sesji w formie słownika
from flask_bootstrap import Bootstrap
import pymysql as mysql 
import random 
import string 
import hashlib # do wyliczania hasha hasła
import binascii # zamiana wartosci binarnych w kod ascii

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "sekretne"

class UserPass: 
    """klasa UserPass przechowuje dane użytkownika"""
    def __init__(self, user='', password=''):
        self.user = user
        self.password = password
        self.email = '' 
        self.is_valid = False # do przechowania info czy konto aktywne, wypelnione
        self.is_admin = False # czy ten user jest adminem
    
    def hash_password (self):
        """funkcja do zahaszowania hasła użytkownika"""
        # salt_random = os.urandom(10) do wygenerowania salt
        salt = b"b\x9a\xec.@\r\x0c\x1c\xbc,+"
        passwordHash = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), salt, 100000)
        passwordHash = binascii.hexlify(passwordHash)
        return passwordHash

    def verify_password(self, stored_password, provided_password):
        """funkcja porównująca przechowane zahaszowane hasło z wprowadzonym przy logowaniu"""
        salt = b"b\x9a\xec.@\r\x0c\x1c\xbc,+"
        passwordHash2 = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
        passwordHash2 = binascii.hexlify(passwordHash2)
        print ("provided_zahasz", passwordHash2)
        return passwordHash2 == bytes (stored_password, 'utf-8') 

    def get_random_user_pasword(self):  
        """funkcja przy inicjacji aplikacji do stworzenie losowego uzytkownika (admina) i jego hasla"""
        random_user = ''.join(random.choice(string.ascii_lowercase)for i in range(5)) 
        self.user = random_user 
        password_characters = string.ascii_letters + string.digits
        random_password = ''.join(random.choice(password_characters)for i in range(5)) 
        self.password = random_password
        print (random_password, 'password wylosowane')
    
    def login_user(self):
        """ funkcja  czy użytkownik jest w bazie danych i czy wprowadzil dobre haslo"""
        con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2")
        cur = con.cursor()
        sqlQuery = "SELECT id, name, email, password, is_active, is_admin FROM `users` WHERE name=%s"
        cur.execute(sqlQuery, [self.user])
        user_record = cur.fetchone()

        if user_record !=None and self.verify_password(user_record[3], self.password):
            return user_record
        else:
            self.user = None
            self.password = None
            return None
    
    def get_user_info (self):
        con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2")
        cur = con.cursor()
        sqlQuery = "SELECT name, email, is_active, is_admin FROM `users` WHERE name=%s"
        cur.execute(sqlQuery, [self.user])
        db_user = cur.fetchone()

        if db_user == None:
            self.is_valid = False
            self.is_admin = False
            self.email = ''
        elif db_user[2] != 1:
            self.is_valid = False
            self.is_admin = False
            self.email = db_user[1] # tuple
        else:
            self.is_valid = True
            self.is_admin = db_user[3]
            self.email = db_user [1]

@app.route("/init_app") 
def init_app():
    """funkcja do startu aplikcji przy 1 razie np. po instalacji"""
    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2")
    cur = con.cursor()
    sqlQuery = "SELECT COUNT(*) as cnt FROM `users` WHERE is_active and is_admin"
    cur.execute(sqlQuery)
    active_admins = cur.fetchone()

    if active_admins[0]>0:
        flash ("Aplication is already set-up. Nothing to do.")
        return redirect(url_for('index'))
    
    # jeśli nie ma admina tworzymy/updatujemy go z kontem i haslem
    user_pass = UserPass() 
    user_pass.get_random_user_pasword()
    sqlQuery = "INSERT INTO `users` (`name`, `email`, `password`, `is_active`, `is_admin`) VALUES (%s, %s, %s, %s, %s);"
    cur.execute(sqlQuery,[user_pass.user, "example@w.com",user_pass.hash_password(), True,True])
    con.commit()
    flash ("User {}  with password {} has been created".format (user_pass.user, user_pass.password))
    return redirect (url_for ("index"))

@app.route("/login", methods = ["GET", "POST"])
def login ():
    """funkcja logowania"""
    login = UserPass (session.get('user') ) # tworzy obiekt dla uzytkownika ktory moze byc teraz w sesji
    login.get_user_info() 

    if request.method == "GET":
        return render_template("login.html", active_menu="login", login=login)
        # login informacja o tym jaki uzytkownik teraz pracuje
    else:
        if "user_name" not in request.form:
            user_name = ""
        else: 
            user_name = request.form["user_name"]

        if "user_pass" not in request.form:
            user_pass = ""
        else: 
            user_pass = request.form["user_pass"]
        
        login = UserPass (user_name, user_pass)
        login_record = login.login_user()

        if login_record !=None:
            session["user"] = user_name 
            """ session sa trzymane w słowniku, dlatego tu przypisanie do klucza user wartosci user_name"""
            flash ("Logon succesfull, welcome {}".format(user_name))
            return redirect (url_for("index"))
        else:
            flash("Logon failed, try again")
            return render_template("login.html", login=login, active_menu = 'login')

@app.route("/logout")
def logout():

    if "user" in session:
        session.pop("user", None) #drugi parametr jest zwracany, jeśli brak pierwszego klucza
        flash ("You are logged out")
    return redirect(url_for("index"))

@app.route("/index", methods=["GET", "POST"])
def index():
    """główna strona bazy danych, wyświetlana jest flota """
    login = UserPass (session.get('user') ) # tworzy obiekt dla uzytkownika ktory moze byc teraz w sesji
    login.get_user_info() 
    try: 
        # połączenie z bazą danych utworzoną w PHPMy Admin  
        con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
        cur = con.cursor()
        sqlQuery = "SELECT id, model, type, reg, year FROM fleet"
        cur.execute(sqlQuery)
        databaseList = cur.fetchall()
        cur.close()
        listLen = len (databaseList)
    except mysql.err.OperationalError as error:
        # wyłapanie wyjątku błędu połączenia z bazą
        print (f"Błąd połączenia:  {error}\n Dane nie zapisane do bazy")
    return render_template ("index.html",databaseList=databaseList, listLen=listLen, login=login, active_menu='Main page') 

@app.route("/add", methods=["GET", "POST"])
def add():
    """dodawanie nowego rekordu w bazie"""
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if login.is_valid is False:
        return redirect (url_for('login'))
    
    if request.method == "GET": # po prostu pierwsze wyświetylenie strony
        return render_template("add.html",login=login)
    else: # jeśli metoda "POST" czyli po wysłaniu formularza
        if "model" in request.form:
            model = request.form["model"] 
        if "type" in request.form: 
            type = request.form["type"]
        if "reg" in request.form: 
            reg = request.form["reg"]
        if "year" in request.form: 
            year = request.form["year"]
        try: 
            con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
            cur = con.cursor()
            sqlQuery1 = "SELECT reg from fleet"
            cur.execute(sqlQuery1)
            regList = [regL[0] for regL in cur.fetchall()]
            if reg in regList:
                flash ("Rejestracja istnieje w bazie")
                con.close()
                return render_template("add.html",login=login)
            else:
                sqlQuery2 = "INSERT INTO `fleet` (`id`, `model`, `type`, `reg`, `year`) VALUES (%s, %s, %s, %s, %s)"
                cur.execute(sqlQuery2, ['NULL', model, type, reg, year])
                con.commit()
                con.close()
                flash ("Dodano do bazy")
                return render_template ("add.html",login=login)
        except mysql.err.OperationalError as error:
            print (f"Błąd połączenia:  {error}\n Dane nie zapisane do bazy")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    """edycja rekordu bazy"""
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if login.is_valid is False:
        return redirect (url_for('login'))

    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
    cur = con.cursor()
    sqlQuery = "SELECT id, model, type, reg, year FROM fleet WHERE id = %s"
    cur.execute(sqlQuery, id)
    record = cur.fetchone()

    if request.method == "GET":
        return render_template ("edit.html", record=record, login=login)
    else:
        if "model" in request.form:
            model = request.form["model"] 
        if "type" in request.form: 
            type = request.form["type"]
        if "reg" in request.form: 
            reg = request.form["reg"]
        if "year" in request.form: 
            year = request.form["year"]

        try: 
            con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
            cur = con.cursor()
            sqlQuery1 = "SELECT reg from fleet"
            cur.execute(sqlQuery1)
            regList = [regL[0] for regL in cur.fetchall()]
            print (f'reglist {regList}' )
            print (f'wprowadzono reg: {reg}')
            if reg == record[3] or reg not in regList:
                sqlQuery2 = "UPDATE `fleet` SET `model` = %s, `type`=%s, `reg` = %s, `year` = %s WHERE `fleet`.`id` = %s"
                cur.execute(sqlQuery2, [model, type, reg, year,id])
                con.commit()
                con.close()
                flash ("Item was changed")
                return redirect(url_for ('index'))

            else:
                flash ("Rejestracja istnieje w bazie, wprowadź dane ponownie")
                con.close()
                return render_template("add.html",login=login)

        except mysql.err.OperationalError as error:
            print (f"Błąd połączenia:  {error}\n Dane nie zapisane do bazy")

@app.route("/search", methods=["GET", "POST"])
def search():
    """wyszukiwanie, wpisana fraza jest traktowana jako fragment łańcucha"""
    if request.method == "GET": # po prostu pierwsze wyświetlenie strony
        return render_template("search.html")
    else:
        if "model" in request.form:
            model = request.form["model"] 
        if "type" in request.form:
            type = request.form["type"] 
        if "reg" in request.form:
            reg = request.form["reg"] 
        if "year" in request.form:
            year = request.form["year"] 

        try: 
            con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
            cur = con.cursor()
            sqlQuery2= f"SELECT * FROM `fleet` WHERE (model LIKE '%{model}%') and (type LIKE '%{type}%') and (reg LIKE '%{reg}%') and (year LIKE '%{year}%')  "
            cur.execute(sqlQuery2)
            databaseList1 = cur.fetchall()
            cur.close()
            listLen = len (databaseList1)
        
        except mysql.err.OperationalError as error:
            print (f"Błąd połączenia:  {error}\n Dane nie zapisane do bazy")

        return render_template ("search_result.html", databaseList1=databaseList1, listLen=listLen)

@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    """wykasowanie rekordu w bazie"""
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if login.is_valid is False:
        return redirect (url_for('login'))#  odc. 40 implement"""
    try: 
        con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
        cur = con.cursor()
        sqlQuery2= f" DELETE FROM `fleet` WHERE `fleet`.`id` = %s  "
        cur.execute(sqlQuery2, [id])
        con.commit()
        cur.close()
        
    except mysql.err.OperationalError as error:
            print (f"Błąd połączenia:  {error}\n Dane nie zapisane do bazy")
    return redirect(url_for("index") )

@app.route("/users")
def users ():
    """wyświetlenie użytkowników, konieczne uprawnienia administratora, czyli is_admin == True"""
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if  login.is_valid == False or login.is_admin == False:
        flash ('Wymagane uprawnienia administratora')
        return redirect (url_for('login'))
    
    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
    cur = con.cursor()
    sqlQuery = "SELECT id, name, email, is_active, is_admin FROM `users`"
    cur.execute(sqlQuery)
    users = cur.fetchall()

    return render_template ('users.html', users=users, login=login)

@app.route ("/user_status_change/<action>/<user_name>")
def user_status_change (action, user_name):
    """funkcja pozwala zmienic pole is_active is_admin dla wybranego uzytkownika"""
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if  login.is_valid == False or login.is_admin == False:
        flash ('Wymagane uprawnienia administratora')
        return redirect (url_for('login'))
    
    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
    cur = con.cursor()
    if action == 'active':      # parametr z route
        sqlQuery = "UPDATE users SET is_active = (is_active + 1) MOD 2 WHERE name = %s and name <> %s"
        cur.execute(sqlQuery, [user_name, login])
        con.commit()

    elif action == 'admin': # parametr z route
        sqlQuery = "UPDATE users SET is_admin = (is_admin + 1) MOD 2 WHERE name = %s and name <> %s"
        # modulo musi jako MOD, a nie % !
        cur.execute(sqlQuery, [user_name, login])
        con.commit()
    return redirect (url_for ('users'))

@app.route ("/edit_user/<user_name>", methods=["GET", "POST"])
def edit_user (user_name):
    """funkcja do edycji użytkownika """
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if  login.is_valid == False or login.is_admin == False:
        flash ('Wymagane uprawnienia administratora')
        return redirect (url_for('login'))
    
    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
    cur = con.cursor()
    sqlQuery = "SELECT name, email FROM `users` WHERE name = %s"
    cur.execute(sqlQuery, [user_name])
    user = cur.fetchone()
    message = None

    if user == None:
        flash ("No such user")
        return redirect (url_for ('users'))

    if request.method == "GET":
        return render_template('edit_user.html', user=user, login=login)
    else:
        new_email = "" if "email" not in request.form else request.form["email"]
        new_password = "" if "user_pass" not in request.form else request.form["user_pass"]

    if new_email != user[1]:
        sqlQuery = "UPDATE `users` SET email = %s WHERE name = %s"
        cur.execute(sqlQuery, [new_email, user_name])
        con.commit()
        flash ("Email was changed")

    if new_password != "":
        user_pass = UserPass (user_name, new_password)
        sqlQuery = "UPDATE `users` SET password = %s WHERE name = %s"
        cur.execute(sqlQuery, [new_password, user_name])
        con.commit()
        flash ("Password was changed")
    
    return redirect(url_for ('users'))

@app.route ("/delete_user/<user_name>") # tu przyjdzie parametr user_name z users.html
def delete_user (user_name):
    """funkcja wykasowanie użytkownika"""
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if  login.is_valid == False or login.is_admin == False:
        flash ('Wymagane uprawnienia administratora')
        return redirect (url_for('login'))
    
    login = session ['user'] # nazwa aktualnego użytkownika
    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2") 	
    cur = con.cursor()
    sqlQuery= " DELETE FROM `users` WHERE name = %s and name <> %s"
    # usuń usera o nazwie, ale który nie jest zalogowany obecnie
    cur.execute(sqlQuery, [user_name, login])
    con.commit()
    
    return redirect(url_for ('users'))

@app.route ("/new_user",  methods=["GET", "POST"])
def new_user ():
    """dodanie nowego użytkownika"""
    login = UserPass ( session.get ('user') )
    login.get_user_info ()
    if login.is_valid is False:
        return redirect (url_for('login'))

    con = mysql.connect(host="127.0.0.1", user="root", passwd="", db="aircraft2")
    cur = con.cursor()
    message = None
    user = {}

    if request.method == "GET":
        return render_template ("new_user.html", active_menu="users", user=user)
    else: # wypelnienie slownika user
        if not 'user_name' in request.form:
            user['user_name'] = '' 
        else:
            user['user_name'] = request.form ['user_name']

        if not 'email' in request.form:
            user['email'] = '' 
        else:
            user['email'] = request.form ['email']

        if not 'user_pass' in request.form:
         user['user_pass'] = ''  
        else:
            user['user_pass'] = request.form ['user_pass']

        #poniżej sprawdzenia przesyłanych danych, czy user jest bazie 
        sqlQuery = "SELECT COUNT(*) as cnt FROM `users` WHERE name = %s"
        cur.execute(sqlQuery, [user['user_name'] ] )
        record = cur.fetchone()
        is_user_name_unique = (record[0] == 0 ) # zwraca True lub False !

        sqlQuery = "SELECT COUNT(*) as cnt FROM `users` WHERE email = %s"
        cur.execute(sqlQuery, [user['email'] ] )
        record = cur.fetchone()
        is_user_email_unique = (record[0] == 0 )

        if user['user_name'] == '':
            message = "Name cannot be empty"
        elif user['email'] == '':
            message = "Email cannot be empty"
        elif user ['user_pass'] == '':
            message = "Password cannot be empty"
        elif not is_user_name_unique:
            message = "User with name {} already exists".format (user['user_name'])
        elif not is_user_email_unique:
            message = "User with email {} already exists".format (user['email'])

        # jeśli żadne z powyższych nie spowodowało wypełnienie message to
        if not message:
            user_pass = UserPass ( user['user_name'], user ['user_pass'] )
            sqlQuery = "INSERT INTO `users` (`name`, `email`, `password`, `is_active`, `is_admin`) VALUES (%s, %s, %s, %s, %s);"
            cur.execute(sqlQuery,[user['user_name'], user ['email'], user_pass.hash_password(), True,False])
            con.commit()
            flash ("User {} created".format(user ['user_name'] ) )
            return redirect (url_for('users'))
        else:
            flash ('Correct error: {}'. format (message))
            return render_template ('new_user.html', user=user, login=login)

if __name__=="__main__":
    app.run()

        elif user ['user_pass'] == '':
            message = "Password cannot be empty"
        elif not is_user_name_unique:
            message = "User with name {} already exists".format (user['user_name'])
        elif not is_user_email_unique:
            message = "User with email {} already exists".format (user['email'])

        # jeśli żadne z powyższych nie spowodowało wypełnienie message to
        if not message:
            user_pass = UserPass ( user['user_name'], user ['user_pass'] )
            sqlQuery = "INSERT INTO `users` (`name`, `email`, `password`, `is_active`, `is_admin`) VALUES (%s, %s, %s, %s, %s);"
            cur.execute(sqlQuery,[user['user_name'], user ['email'], user_pass.hash_password(), True,False])
            con.commit()
            flash ("User {} created".format(user ['user_name'] ) )
            return redirect (url_for('users'))
        else:
            flash ('Correct error: {}'. format (message))
            return render_template ('new_user.html', user=user, login=login)


if __name__=="__main__":
    app.run()
