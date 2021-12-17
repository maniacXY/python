
from replit import clear
import time
#create top numbers
field = [["| |", "|1|", "|2|", "|3|"]]
#create gamefield
for i in range(3):
    field.append([f"|{i+1}|" ,"| |", "| |", "| |"])
#function show gamefield
def gamefield():
    n=0
    for num in range(len(field)):
        print(field[num][0], field[num][1], field[num][2], field[num][3])
        n+=1

def changegamefield(sign, field, player):
    print(f"Make a Choice!\nSpieler {player} hat das Symbol {sign}")
    vert=int(input("vertikale Nummer: "))
    hor=int(input("horizontale Nummer: "))
    if vert > len(field)-1 or hor > len(field)-1:
        print("Fuck You")
        changegamefield(sign, field, player)
    if field[vert][hor] == "|x|" or field[vert][hor] == "|o|":
        clear()
        print("Schon belegt!")
        gamefield()
        changegamefield(sign, field, player)
    else:
        clear()
        field[vert][hor]=f"|{sign}|"
        gamefield()
        
#Vertical check
def vertical_check():
    a = 0
    b = 0
    for i in range(1,len(field)):
        for items in field [i]:
            if items == "|x|":
                a +=1
            elif items == "|o|":
                b +=1
    if a == 3:
        print("A WIN")
        return True
    elif b == 3: 
        print("B Win")
        return True
        

# #horizontal check
# def horizontal_check():
#     a = 0
#     b = 0
#     for i in range(1,len(field)):
#         for items in field[i]:
            
#             if items == "|x|":
#                 a +=1
#             elif items == "|o|":
#                 b +=1
#     if a == 3:
#         print("A WIN")
#     elif b == 3: 
#         print("B Win")

def cross_check():
    a=0
    b=0
    count = len(field)-1

    for item in range(1,len(field)):
        if field[item][item] == "|x|" or field[count][item] == "|x|":
            a +=1
            
        elif field[item][item] == "|o|" or field[count][item] == "|o|":
            b +=1
            
        count -=1
        
    if a == 3:
        print("A WIN")
        return True
    elif b == 3: 
        print("B Win")
        return True

def checking():
    if vertical_check() or cross_check() == True:
        print("Danke fürs Spielen")
        time.sleep(3)
        game()
    else: 
        return True
    # horizontal_check()
   


#GAME START
def game():
    clear()    
    print("Herzlich Willkommen zu TicTacToe")
    start=input("Bock auf ne Runde? y/n?: ")
    if start == "n":
        exit()
    elif start == "y":
        player1 = input("Wie ist der Name von Spieler 1?: ")
        player2 = input("Wie ist der Name von Spieler 2?: ")
        gamefield()
        gamestate = True   
        rounds = 0
        while gamestate:
            spieler = "x"
            changegamefield(spieler, field, player1)
            gamestate = checking()
            spieler = "o"
            changegamefield(spieler, field, player2)
            gamestate = checking()
            rounds +=1
            if rounds == 9:
                print("Unentschieden, Spiel wird neugestartet")
                time.sleep(3)
                game()
    else: 
        print("Diese Option ist nicht verfügbar")

game()


 
