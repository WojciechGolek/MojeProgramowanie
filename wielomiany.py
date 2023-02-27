"""Mnożenie wielomianów  - program przydatny w nauce na poziomie maturalnym lub
ponadmaturalnym do kontroli wykonanych działań
"""
import numpy

class incorrectDate (Exception):
    pass


def mulPoly(n):

    lista = []
    lista2 =[]
    array = numpy.zeros((2,n+1)) 
    """ utworzenie tablicy 2 wierszowej, n elementowej 
    potęga najwyższa+1 w wierszu  i wypełnienie zerami"""
    print ("Podaj współczynniki obu wielomianów: ")
    """wylistowanie formatu wielomianów dla ułatwienia"""
    for i in range (0,n):
        z = (f"{chr(97+i)}*x^{n-i}")
        lista.append (z)
    lista.append (chr(97+n))
    print (lista)
    
    try:
        for j in range(2):
            for i in range(n+1):
                z = input (f"Podaj współczynnik {chr(97+i)}{j+1}: ")
                if float(z):
                    array[j][i] = z
    except ValueError:
        print ("Błędny format danych")
        quit()

    """utworzoną tablice array dzielimy na dwie, celem wykorzystania
    funkcji z biblioteki numpy"""
    array1 = (array[0])
    array2 = (array[1])

    mulPol = numpy.polymul(array1, array2)
    leng = len (mulPol)

    for i in range (0,leng-1):
        z = (f"{mulPol[i]}*x^{leng-i-1}")
        lista2.append (z)
    x = int( mulPol [leng-1])
    lista2.append (x)
    """Pokazanie formatu wynikowego wielomianu wraz z podstawieniem współczynników"""
    print (f"Wielomian wynikowy:\n {lista2}")

def main():
       
    try:
        n = int (input ("Podaj najwyższą potęgę w wielomianach: ") )
        """podajemy najwyższą potęgę występująca w wielomianach 
        celem utworzenia tablicy pomocniczej do obliczeń"""
        if n <= 0:
            raise incorrectDate()
        else:
            mulPoly(n)
    except ValueError:
        print ("Błędny format danej. Koniec.")
        quit()
    except incorrectDate:
        print ("Błędny format danej. Koniec.")
    

if __name__ == "__main__":
    main ()
