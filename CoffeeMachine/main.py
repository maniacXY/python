import data
from art import text, coffeart, notav, shutdown
from replit import clear
import time



MENU = data.MENU
meinangebot = " / ".join([x.capitalize() for x in MENU.keys()])
RESOURCES = data.resources
MONEY = 0
REFILLCODE = 123

def support(userinput, resources, money=MONEY):
    if userinput == "quit":
        clear()
        print(shutdown)
        time.sleep(3)
        exit()
    else:
        clear()
        for key in resources.keys():
            if key == "coffee":
                print(f"{(key).capitalize()}: {resources[key]} g ")
            else:
                print(f"{(key).capitalize()}: {resources[key]} ml ")
        print(money)
        time.sleep
        machine()

def enough_resources(resources, menu_userinput):
    for key in resources:
        result = resources[key] - menu_userinput[key]
        if result <=0:
            return False
        else:
            return True
            

def refill():
    refilling = int(input("'0' for Shutdown; Refill done, money cleared enter the code: "))
    if refilling == 0:
        prozessed = True
        support('quit')
    elif refilling == REFILLCODE:
        prozessed = True
        clear()
        print("Refilling done, rebooting the machine")
        time.sleep(2)
        
    else:
        print("Parameter not defined")
        refill()


def calculation(euro, cent, productprice):
    moneysum = euro + cent / 100
    ergebnis = productprice - moneysum
    if moneysum < productprice:    
        print("Less money ... I miss {ergebnis} €")
        return False
    else: 
        return True

def resources_left(resources, userchoice):
    for key in resources:
        if key in userchoice:
            resources[key] = resources[key] - userchoice[key]
    return resources 




def machine():
    print("FUCK YOU")
    print(RESOURCES)
    resources = RESOURCES
    print(resources)
    money = MONEY
    running = True
    while running: 
        
        userinput = (input(f"What would you like? ({meinangebot}): ")).lower()
        if userinput == "report" or userinput == "quit":
            support(userinput, resources, money)
        elif userinput in MENU.keys():
            if enough_resources(resources, MENU[userinput]['ingredients']):
                print(f"Produkt: {userinput.capitalize()}\nPreis: {MENU[userinput]['cost']} €")
            else:
                refill() 
                machine()
                
        else:
            print("not available, or typo")
            machine()
        
        enough_money = False
        while not enough_money:
            print("Please insert the coins\n------------------------")
            print("'x' for abort")
            euro = int(input("Wie viel Euromünzen?: "))
            cent = int(input("Wie viel Centmünzen?: "))
            enough_money = calculation(euro, cent, MENU[userinput]['cost'])
        clear()
        print(coffeart)
        print(f"Serving {userinput.capitalize()}, have a nice day! ")

        # some prozessing
        # resources = resources_left(resources, MENU[userinput]['ingredients']) 
        money += MENU[userinput]['cost']

machine()


## Was läuft noch nicht.
# Wechselgeld fehlt
# Resources werden nicht korrekt abgezogen bzw aufgefüllt ..
# Geldeinnahmen bis zum nächsten Refill passen auch nicht
# Bilder fehlen noch 