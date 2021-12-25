from datetime import date, datetime
from typing import Text
from replit import clear

TXTFILE = "data_dailytask.txt"
TEXTINFILE = []

#read file and store it into TEXTINFILE
def read_file_out():
    """return tmplist with file text"""
    tmplist=[]
    with open(TXTFILE) as file: 
        for i in file.readlines():
            tmplist.append((i.strip().split(",")))
    return tmplist

#Ask user for Date and give it in STR back 
def menu1():
    """return strdatechoice"""
    strdatechoice = ""
    choice = input("Heute(1), anderes Datum(2): ")
    
    if choice == "1":
        today = datetime.now()
        strdatechoice = today.strftime("%Y")+"-"+today.strftime("%m")+"-"+today.strftime("%d")
        print()
        
    elif choice == "2":
        strdatechoice = input("Welche Datum? yyyy-mm-dd: ")
        print()
        
    else: 
        print("NA, again pls")
        menu1()
    
    return strdatechoice
        
def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)

def readydone(state="not"):
    if state == "finish":
        print("\nYou got it :-*\n")
    
    for i in range(len(TEXTINFILE)):
        if date == TEXTINFILE[i][0]:
            print(*TEXTINFILE[i])



clear()
print("Welcome to Daybook!\n")
TEXTINFILE = read_file_out()

allright = False
while not allright: 
    
    date = menu1()

    readydone()

    zeit = input("\nGibt die Uhrzeit ein. hh:mm-hh:mm ")
    text = input("Gibt den Text ein: ")
    print(f"\nDeine Eingabe ist: {date} {zeit} {text}")
    choice = (input("Alles korrekt? y/n: ")).lower()
    if choice == "y":
        break
 
TEXTINFILE.append([date,zeit,text])
TEXTINFILE.sort() 

with open(TXTFILE, "r+") as f:
    f.truncate(0)

for i in range(len(TEXTINFILE)):
    a = ','.join(TEXTINFILE[i])
    append_new_line(TXTFILE, a)

readydone("finish")

TEXTINFILE.clear()






