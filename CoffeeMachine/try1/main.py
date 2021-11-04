import data
import keyboard
from art import text, coffeart, notav, shutdown
from replit import clear
import time





def support(REFILLCODE="1234"):
    print("Machine under maintenance")
    print("Please call the secretary for refilling the Machine")
    refill_done = False
    while not refill_done:
        enter_code = input("If refilling done enter the code: ")
        if REFILLCODE == enter_code:
            refill_done = True
    machine()


def user_vs_resources(RESOURCES, MENU, userchoice):
    """checks wheater enough resources are available, return True or False"""
    menu_values = MENU[userchoice]["ingredients"]
    for key in menu_values:
        ergebnis = RESOURCES[key] - menu_values[key]
        if ergebnis <= 0:
            print(f"Sorry not enough resources. Please refill")
            output_report(RESOURCES, "report")
            support()
    print(f"The price for a {userchoice.capitalize()} is {MENU[userchoice]['cost']} € ")
    return True

def money_enough(MENU, userchoice, euro, cents):
    sum_euro = 1 * euro
    sum_cents = cents / 100
    sum_money = sum_euro + sum_cents
    calculation = MENU[userchoice]["cost"] - sum_money
    if calculation > 0:
        print("Not enough Money!")
        return False
    else:
        returncents = round(((calculation)*-1%1)*100)
        returneuro = int((calculation + calculation * -1 % 1) * -1)
        print(f"You get {returneuro} € and {returncents} Cents back ")
        print(f"Enjoy your {userchoice}. Have a nice day!")
        time.sleep(6)
        return True

def output_report(RESOURCES, userchoice, MONEY=0):
    """Formats the output string from RESSOURCES"""
    if userchoice == "report":
        output = ""
        for key in RESOURCES:
            if key == "coffee":
                output += f"{key.capitalize()}: {RESOURCES[key]}g\n"
            else:
                output += f"{key.capitalize()}: {RESOURCES[key]}ml\n"
        output += f"Money: {MONEY} €"
        print (output)
        time.sleep(3)
        
    elif userchoice == "quit":
        clear()
        print(shutdown)
        time.sleep(3)
        quit()

def track_resource(userchoice, RESSOURCES, MENU):
    menu_values = MENU[userchoice]["ingredients"]
    for key in menu_values:
        RESSOURCES[key] = RESSOURCES[key] - menu_values[key]


    return RESSOURCES




def machine():
    MENU = data.MENU
    meinangebot = " / ".join([x.capitalize() for x in MENU.keys()])
    RESOURCES = data.resources
    MONEY = 0
    REFILLCODE = "1234"
    print(RESOURCES)
    
    running = True
    while running:
        
        userinput = True
        while userinput:
            # clear()
            print(text)
            print(coffeart)
            userchoice = (input(f"What would you like? ({meinangebot}): ")).lower()
            if userchoice == "report" or userchoice == "quit":
                output_report(RESOURCES, userchoice, MONEY)
            elif userchoice in MENU.keys():
                userinput = False
            else:
                clear()
                print(notav)
                print("Choose again!")
                time.sleep(3)
        enough_resources = user_vs_resources(RESOURCES, MENU, userchoice)
        if not enough_resources:
            support(REFILLCODE)
        RESOURCES = track_resource(userchoice, RESOURCES, MENU)
        print(RESOURCES)
        enough_money = False
        while not enough_money:
            print("Please insert coins.")
            euro = int(input("How many Euro?: "))
            cents = int(input("How many Cents?: "))
            enough_money = money_enough(MENU, userchoice, euro, cents)
        MONEY += MENU[userchoice]["cost"]
        

machine()
