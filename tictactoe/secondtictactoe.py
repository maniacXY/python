from replit import clear
import time



#Main VARS
PLAYER1=""
PLAYER2=""
signplayer1 = "x"
singplayer2 = "o"

        
#create gamefield[0]
GAMEFIELD = [["   ", "|1|", "|2|", "|3|"]]
#create gamefield rest
for i in range(3):
    GAMEFIELD.append([f"|{i+1}|", "| |", "| |", "| |"])

def createnew ():
    field = [["   ", "|1|", "|2|", "|3|"]]
#create gamefield rest
    for i in range(3):
        field.append([f"|{i+1}|", "| |", "| |", "| |"])
    return field

#function show gamefield
def showgame():
    n=0
    for num in range(len(GAMEFIELD)):
        print(GAMEFIELD[num][0], GAMEFIELD[num][1], GAMEFIELD[num][2], GAMEFIELD[num][3])

list = GAMEFIELD
# print("Hello and Welcome to TicTacToe\n")
# PLAYER1 = input("What is the name of player 1? : ")
# PLAYER2 = input("What is the name of player 2? : ")

#check playerinput return nothing
def turn(signplayer):
    showgame()
    #inputs
    vertical = int(input("Vertical number: "))
    horizontal = int(input("Horizontal number: "))
    #check inputs
    if vertical < 1 or vertical > len(GAMEFIELD)-1:
        clear()
        print(f"{vertical} existiert nicht bitte nochmal!")
        time.sleep(3)
        turn(signplayer)
    if horizontal < 1 or horizontal > len(GAMEFIELD)-1: 
        clear()
        print(f"{horizontal} existiert nicht bitte nochmal!")
        time.sleep(3)
        turn(signplayer)
    #check double signs
    if GAMEFIELD[vertical][horizontal] != "| |":
        clear()
        print(f"Das Feld {vertical}|{horizontal} ist schon belegt, bitte nochmal!")
        turn(signplayer)
    else: 
        GAMEFIELD[vertical][horizontal] = f"|{signplayer}|"
        






def checktable (player, signplayer):
    game = "run"
    
    #horizontal check
    for i in range(1,4):
        if GAMEFIELD[i].count(f"|{signplayer}|") == 3:
            showgame()
            print(f"Gratulation {player} gewinnt!")
            game = "over"
            break
    
    #vertical check
    if game == "run":
        templist = []
        for num in range(1,4):
            templist = [GAMEFIELD[num][1], GAMEFIELD[num][2], GAMEFIELD[num][3] ]
            if templist.count(f"|{signplayer}|") == 3:
                showgame()
                print(f"Gratulation {player} gewinnt!")
                game = "over"
                break
    #crosscheck
    if game == "run":
        templist = []
        #left to right
        for num in range(1,4):
            templist.append(GAMEFIELD[num][num])
            if templist.count(f"|{signplayer}|") == 3:
                showgame()
                print(f"Gratulation {player} gewinnt!")
                game = "over"
                break
        #right to left
        if game == "run":
            templist = []
            i = 3
            for num in range (1,4):
                templist.append(GAMEFIELD[num][i])
                i-=1
                if templist.count(f"|{signplayer}|") == 3:
                    showgame()
                    print(f"Gratulation {player} gewinnt!")
                    game = "over"
                    break
    #return Game still running
    if game == "run":
        return True
    else: 
        return False



def game():
    clear()
    list = createnew()
    GAMEFIELD = list
    gamerunning = True
    while gamerunning:
        turn(signplayer1)
        gamerunning = checktable(PLAYER1, signplayer1)
        if gamerunning:
            turn(singplayer2)
            gamerunning = checktable(PLAYER2, singplayer2)
    
    again = (input("Vielen Dank fürs Spielen noch eine Runde? y/n: ")).lower()
    if again == "y":
            game()
            
            
    else: 
        exit()

game()