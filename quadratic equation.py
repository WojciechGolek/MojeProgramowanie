"""program do rozwiązywania równań kwadratowych,
może być pomocny w nauce matematyki w szkołach ponadpodstawowych"""

import math

class QuadEquation:
    "klasa , do której przekazuje się parametry równania podane przez usera"

    def __init__ (self, aFac, bFac, cFac):
        self.aFac = aFac
        self.bFac = bFac
        self.cFac = cFac

    def solution (self):
        if self.aFac == 0 and self.bFac == 0:
            return (f"Brak rozwiązań. Układ niejednoznaczny.")
        if self.aFac == 0:
            x1 = round(-self.cFac/self.bFac,3)
            return (f"Jedno rozwiązanie x = {x1}")
        
        delt = pow(self.bFac,2) - (4*self.aFac*self.cFac)
        if delt == 0:
            x = -self.bFac / (2*self.aFac)
            return x
        if delt < 0:
            return (f"Brak rozwiązań równania")
        if delt > 0:
            x1 = round ((-self.bFac-math.sqrt(delt))/2*self.aFac,3)
            x2 = round ((-self.bFac+math.sqrt(delt))/2*self.aFac,3)
            return (f"rozwiązania {x1} i {x2}")


def main(): 
    try:
        print ("Podaj współczynniki równania a, b, c \nszyk a*x^2 b*x c oddzielając spacją ")
        a, b, c = input().split(" ")
        a = float (a); b = float (b); c = float (c)
    except ValueError:
        print ("Błędny format danych. Spróbuj ponownie.")
        quit ()
    
    print (QuadEquation (a, b, c).solution())

if __name__ == "__main__":
    main ()



