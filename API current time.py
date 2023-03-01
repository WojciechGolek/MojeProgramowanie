"""program wykorzystujący ogólnodostępne API https://www.timeapi.io/swagger/index.html
i podaje aktualny czas dla pobranych od użytkownika współrzędnych geograficznych"""

import requests
from terminaltables import AsciiTable

def coordinates():
    #pobranie danych od usera i obsługa możliwych nieprawidłowiści w danych
    try:
        print ("Podaj współrzędne miejsca: \nszerokość geograficzna zakres -90,90 \ni długość geograficzna zakres -180,180")
        lat = float( input ("Szerokość: "))
        long = float(input ("Długość: "))
    
        if lat not in range (-90,91) or long not in range (-180,181) :
            raise Exception ("Dane spoza zakresu")
        
    except ValueError:
        print ("Błędny format danych")
        
    except Exception as e: 
        print (e)

    url (lat, long)

def url(lat, long): 
    # funkcja wykonująca połączenie API i wyświetlająca dane
    str1 = ""
    response = requests.get (f"https://www.timeapi.io/api/Time/current/coordinate?latitude={lat}&longitude={long}")
    if response.ok == True:
        print ("ok")
        dane = response.json()

    hour = dane ["hour"]
    minute = dane ["minute"]
    if minute < 10: minute = "0" + str(minute)
    second = dane ["seconds"]
    if second < 10: second = "0" + str(second)
    timeZone = dane ["timeZone"]
    str1 = f"{hour}:{minute}:{second}"
    
    table_print = [
    ["strefa czasowa", "godz:min:sek"],
    [timeZone, str1]
    ]
    table = AsciiTable(table_print)
    print (table.table)

if __name__ == "__main__":
    coordinates()