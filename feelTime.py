"""Program dla zabawy, sprawdzający wyczucie czasu gracza. Należy 
wyłapać wylosowany interwał czasu z przedziału 1- 6 sekund. """

import tkinter as tk
import random
import time

tInterval = 0
tDelta = 0
tList = []
t = random.randint (1,6)

"""funkcje Start i Stop notują znacznik czasu i tworzą z nich listę 2-elem"""
def Start (button):
    global tList
    tStart = time.time()
    tList.append(tStart)
    button1["state"]="disabled"

def Stop (button):
    global tList
    tStop = time.time()
    button2["state"]="disabled"
    tList.append(tStop)
    if len (tList) == 2:
        CountingTime ()
    return

"""funkcja obliczająca różnicę złapanego czasu i przyrównująca do zadanego interwału"""
def CountingTime():
    global t
    tDelta = tList[1] - tList[0]
    tDelta = round (tDelta, 2)
    tInterval = tDelta - t
    t = 0
    if tInterval > 0:
        comment = f"zatrzymano stoper za późno o {round (tInterval, 2)} sek\n"
        label2.config (text=comment)
    elif tInterval < 0:
        comment = f"zatrzymano stoper za wcześnie o {abs(round (tInterval,2))} sek\n"
        label2.config (text=comment)
    else:
        comment = f"idealnie w punkt"
        label2.config (text=comment)

"""funkcja umożliwiająca ponowną grę"""
def reset1 (button3):
    global run
    global t
    global tDelta
    global tInterval
    global tList
    run = True
    t = random.randint (1,5)
    tList=[]
    tInterval = 0
    tDelta = 0
    label1.config (text=f"Skoncentruj się! \nInterwał czasu do wyłapania:\n {t} sek")
    label2.config (text="")
    button2.config (state = "normal")
    button1.config (state = "normal")

window = tk.Tk ()
window.geometry ("380x380")
label = tk.Label (window)
window.title ("Wyczucie czasu")

label1 = tk.Label (window, 
            text = f"Skoncentruj się! \nInterwał czasu do wyłapania:\n {t} sek",
            foreground="black",
            bg = "grey",
            width = 25,
            height = 3,
            font = "Times 15 bold italic",
            padx = 5, pady = 5)
label1.place(x=55, y=20)

label2 = tk.Label (window, 
            text = "",
            foreground="black",
            bg = "grey",
            width = 35,
            height = 2,
            font = "Times 13 bold italic",
            padx = 2, pady = 5)
label2.place(x=15, y=220)

button1 = tk.Button (
                window,
                text = "Start",
                state="normal",
                border = 5,
                fg = "black",
                bg = "light grey",
                activeforeground= "black",
                activebackground= "red",
                font = "Times 17 italic",
                height = 2,
                width= 10,
                padx= 8,
                pady= 8,
                relief= "groove",
                command =lambda: Start(button1))
button1.place(x=50, y=115)

button2 = tk.Button (
                window,
                text = "Stop",
                border = 5,
                fg = "black",
                bg = "light grey",
                activeforeground= "black",
                activebackground= "red",
                font = "Times 17 italic",
                height = 2,
                width= 10,
                padx= 8,
                pady= 8,
                relief= "groove",
                command = lambda: Stop(button2))
button2.place(x=190, y=115)

button3 = tk.Button (window, bg = "white", 
                fg = "black", 
                text = "Wyjście",
                activeforeground= "black", 
                activebackground= "red",
                font = "Times 13 italic", 
                height = 2, 
                width= 10,
                padx= 2, pady= 2, 
                command = quit)
button3.place(x=50, y=300)

button4 = tk.Button (window, bg = "white", 
                fg = "black", 
                text = "Gramy jeszcze raz",
                activeforeground= "black", 
                activebackground= "red",
                font = "Times 13 italic", 
                height = 2, 
                width= 20,
                padx= 2, pady= 2, 
                command = lambda: reset1(button3) )
button4.place(x=160, y=300)
    
window.mainloop ()








