from replit import clear

class Kassensystem:
    __preise = {
    "Wasserflasche": 1.0,
    "Multisaft": 1.20,
    "Kindercountry": 0.49,
    "TK-Pizza": 1.49
    }
    
    def __init__(self):

        self.warenkorb = []
        self.sum = 0
    
    def product_print(self):
        for k in self.__preise.keys():
            print(k.ljust(10))

    def price_to_string(sefl,price):
        price = str(round(float(price),2))
        splitted = price.split(".")
        first = splitted[0].rjust(3,' ')
        second = splitted[1].ljust(2,"0")
        return(first+"."+second+"€")
    
    def add_article(self,article, anzahl):
        product_price = self.__preise[article]
        summe = product_price * anzahl
        self.sum += summe
        item = [anzahl, article,product_price, summe ]
        self.warenkorb.append(item)
        for entry in self.warenkorb:
            print(self.entry_to_string(entry))
        
    def header(self):
        print("Produkt".center(20),"a".ljust(12),"EUR")
        print(40*"-")
    def footer(self):
        print(40*"-")
        print("Summe:".rjust(31),self.price_to_string(self.sum))
        
    def kassenzettel(self):
        clear()
        self.header()
        for item in self.warenkorb:
            print(self.entry_to_string(item))
        self.footer()
    
    def entry_to_string(self, item):
        return f"{str(item[0]).rjust(2)}x {item[1].ljust(14)} {self.price_to_string(item[2]).ljust(13)}{self.price_to_string(item[3])}"
kasse = Kassensystem()


eingabe = True
while eingabe: 
    clear()
    kasse.product_print()
    product = input("\nWelches Produkt? ")
     anzahl = int(input("Wie viel? (int)\n"))
    kasse.header()
    kasse.add_article(product, anzahl)
    weiter = input("\nNoch ein Pordukt oder Summe? (y/sum)").lower()

    if weiter == "sum":
        eingabe =False
kasse.kassenzettel()
    


