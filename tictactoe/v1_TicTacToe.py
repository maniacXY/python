# GAME FULL
import time

PLAYER1 = ""
PLAYER2 = ""
SIGNP1 = "x"
SIGNP2 = "o"

def createTable():
    """creates and returns table"""
    table = [[" "," 1 "," 2 "," 3 "]]
    for i in range(3):
        table.append(["| |", "| |","| |"])
    n=1
    for i in range(1,4):
        table[i].insert(0,str(n))
        n+=1
    return table
    
def showTable(table):
    for i in range(len(table)):
        print(" ".join(table[i]))

#Takes Userinput check it and only go on if everything ok
def userinput(sign, table, player):
    """retuns nothing, continue if ok"""
    print(f"\n{player}, your turn with sign {sign}")
    vertical = int(input("Vertikale: "))
    if vertical < 1 or vertical > len(table)-1: 
        print("Not available bitte nochmal eingeben")
        userinput(sign, table, player)
    horizontal = int(input("Horizontale: "))
    if horizontal < 1 or horizontal > len(table)-1: 
        print("Not available bitte nochmal eingeben")
        userinput(sign, table, player)
    if table[vertical][horizontal] != "| |":
        print("Schon belegt bitte nochmal eingeben")
        userinput(sign, table, player)
    else:
        table[vertical][horizontal] = f"|{sign}|"
        showTable(table)

def checktable(sign, player, table):
     
    """If there is a winner return False else True"""
    #vertical
    for i in range (1,4):
        if table[i].count(f"|{sign}|") == 3:
            print(f"3 in a row! {player} wins!!!")
            return False
    #horizontal
    for i in range(1,4):
        a = 0
        for j in range(1,4):
            if table[j][i] == f"|{sign}|":
                a+=1
        if a == 3:
            print(f"3 in a col! {player} wins!!!")
            return False
    #cross check
    #left->right
    a  = 0
    for i in range (1,4):
        
        if table[i][i] == f"|{sign}|":
            a+=1
    if a == 3:
        print(f"3 in a cross left->right! {player} wins!!!")
        return False
    #right -> left
    a = 0
    for i in range (1,4):
        if table[i][i*-1] == f"|{sign}|":
            a+=1
    if a == 3:
        print (f"3 in a cross right->left! {player} wins!!!")
        return False
    return True      

def game():
    table = createTable()
    PLAYER1 = input("P1 Name pls: ")
    PLAYER2 = input("P2 Name pls: ")
    showTable(table)
    gamerunning=True
    turns = 0
    while gamerunning or turns < 5: 
        #p1 turn
        userinput(SIGNP1, table, PLAYER1)
        gamerunning = checktable(SIGNP1, PLAYER1, table)
        if turns == 4:
            print("Unentschieden")
            break
        #p2 turn
        if gamerunning:
            userinput(SIGNP2, table, PLAYER2)
            gamerunning = checktable(SIGNP2, PLAYER2, table)
        turns += 1
    again = (input("Möchtest du noch eine Runde Spielen? y/n")).lower()
    if again == "y":
        print("Na dann los :D. Viel Spaß!")
        time.sleep(2)
        game()
    else: 
        print("Vielen Dank\nSchönen Tag noch!")
        
game()