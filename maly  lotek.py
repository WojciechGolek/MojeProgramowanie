"""gra losowa na zasadzie typowania 3 liczb z zakresu i przyrównaniu 
do wylosowanych przez komputer"""
import random
import time

compListNum = []
userListNum = []
on = True
i = 0
h = 0   
 
print ("\nZACZYNAMY") 

while on:
    print ("Podaj swoje liczby z zakresu 1 - 20 oddzielone spacją")
    userNum1, userNum2, userNum3 = input ("lub 0 0 0 na exit: \n\n").split (" ")
    userNum1 = int (userNum1); userNum2 = int (userNum2); userNum3 = int (userNum3)
    if userNum1 == 0 and userNum2 ==0 and userNum3 == 0: break
    
    if (userNum1 < 1 or userNum1 > 20 or userNum2 < 1 or userNum2 > 20 or userNum3 < 1 or userNum3 > 20) or (userNum1 == userNum2 or userNum1 == userNum3 or userNum2 == userNum3):
        print ("\nLiczby powtarzaja się lub są spoza zakresu, spróbuj ponownie".upper() )
        on = True
    
    else:
        userListNum.extend ( [userNum1, userNum2, userNum3] )
  
        print ("\n")
        while h < 3:
            num = random.randint(1, 20)
            if compListNum.count (num) == 0:
                compListNum.append (num)
                h = h + 1
        print ("Uwaga! Komputer losuje:\n ")
                
        for j in compListNum:
            print (j)
            time.sleep (1) # funkcja usypia watek programu na zadaną ilość sekund
            j +=1
        
        on = False

        for x in compListNum:
            for z in userListNum:
                if x == z:
                    i += 1
        if i > 0:
            if i == 1:
                print ("\nNieźle, zgadłaś", i, "liczbę\n")
                quit ()
            if i == 2:
                print ("\nBrawo, zgadłaś", i, "liczby\n") 
                quit ()
            else:
                print ("\nPełna wygrana, zgadłaś wszystkie liczby\n")       
            quit()

        if i == 0:
            print ("\nBrak trafienia.\n")
            
        print ("Próbujesz ponownie t / n:")
        z = input ()
        if z == "t":
            on = True
            compListNum = []
            userListNum = []
            h = 0
        else:
            on = False
        


        
        
        
    














    

