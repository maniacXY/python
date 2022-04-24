from ast import Index
from tkinter import *
from tkinter import ttk
from time import sleep
from playsound import playsound
import sys
import os

NAME_OF_TIMER = "My Timer"
SCRIPT_DIR = "/home/USER/../.../"
NAME_OF_SOUND = "schulglocke.mp3"

try:
    x = sys.argv[1]
except IndexError:
#DEFAULT TIME
    x = "10"

def formatter(y):
    y = y.split(":")
    minuten = int(y[0])*60
    sekunden = int(y[1])
    return minuten+sekunden
    
def reset(x=10):
    try:
        zeit = formatter(x)
    except IndexError:
        zeit = int(x)
    while zeit > -1:
        timer.config(text='%02d' %(zeit//60)+":"+ '%02d'%(zeit%60))

        zeit-=1
        root.update()
        sleep(1)
    os.chdir(SCRIPT_DIR)
    playsound(NAME_OF_SOUND)
    root.destroy()  
root = Tk()
root.geometry("200x150")
root.title("Timer")
frm = ttk.Frame(root)
frm.grid(padx=25)
ttk.Label(frm, text=NAME_OF_TIMER, font=("Arial", 25,"bold")).grid(column=0, row=0, pady=5, columnspan=3)
timer = ttk.Label(frm, text="Hello World!", font=("Arial", 20,"bold"))
timer.grid(column=1, row=1, sticky="")
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2, pady=10)
root.after(1000, reset(x))
root.mainloop()



