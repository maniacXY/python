
from time import sleep
from replit import clear
import pandas as pd
import json

class DataChecker:
    def __init__(self) -> None:
        self.config = self.load_config_data("config.json")
        self.csv_data = pd.read_csv(self.config["csv_data"], sep=self.config["sep"])
    
    # läd json data
    def load_config_data(self, configdata): 
        with open(configdata, "r") as config:
            return json.load(config)
    
    # create a new item
    def create_item(self):
        clear()
        print("Create Your Item\n")
        tmp_list = []
        tmp_dict = {}
        indexing = 0  
        #read the keys,print them and ask for the values u wanna create
        for key in self.csv_data.keys():
            tmp_list.append(key)
            tmp_dict[key]= input(f"{str(indexing).rjust(2)} {key.ljust(15)}: ")
            indexing +=1
        #here u can change the data if u want 
        correct = False
        while not correct: 
            clear()
            for item in tmp_list:
                print("{} {}: {}".format(str(tmp_list.index(item)).rjust(2),item.ljust(15),tmp_dict[item]))
            right = input("\nIs everything correct? (y/n/quit): ").lower()
            
            # store it in class att and save it to .json
            if right == "y":
                self.csv_data = self.csv_data.append(tmp_dict, ignore_index=True)
                self.save_csv()
                correct=True
            elif right =="quit":
                exit()
            #change value block
            else:                
                try:
                    user_index = int(input("What Index u wanna change? "))
                except ValueError: 
                    print("Bitte nur Zahlen eingeben! INT")
                    continue   
                if user_index >= 0 and user_index < len(tmp_list):
                    value = input(f"{tmp_list[user_index].ljust(15)}: ")
                    tmp_dict[tmp_list[user_index]] = value          
                else:
                    print("Index nicht vorhanden")
    
    def change_item(self):
        clear()
        print("Change ITEM")
        sleep(2)
        # Erster While Loop für neue Einträge
        correct = False
        while not correct: 
            print(self.csv_data)
            user_index = input("Welche Indexnummer willst du ändern? (INT/quit/save): ").lower()
            try: 
                user_index = int(user_index)
            except ValueError:
                if user_index == "quit":
                    exit()
                elif user_index == "save":
                    self.save_csv()
                    break
                else:
                    print("Nur INT-Wert")
                    continue
            clear()
            print(self.csv_data.loc[user_index])
            
            #Möglichkeit den aktuellen Eintrag nochmal zu ändern
            zufrieden = False
            while not zufrieden:
                user_key = input("Was möchtest du ändern? ").lower()
                
                try:
                    if user_key == "status":
                        value = self.change_status(self.csv_data.loc[user_index])
                    else:
                        print("\nAlter Eintrag -> Neuer Eintrag")
                        value = input(f"{self.csv_data.loc[user_index][user_key]} -> ")
                except KeyError:
                    print("Achte bitte auf die Rechtschreibung")
                    continue
                self.csv_data.loc[user_index] = self.csv_data.loc[user_index].replace([self.csv_data.loc[user_index][user_key]], value)
                clear()
                
                print(self.csv_data.loc[user_index])
                ok = input("\nZufrieden? (y/n/quit): ").lower()
                if ok == "y":
                    zufrieden = True
                elif ok == "quit":
                    exit()
                else: 
                    continue
            clear()
            #Loop wird wiederholt wenn y
            ok = input("Möchtest du noch weitere Daten ändern? (y/n/quit): ").lower()
            if ok == "y":
                continue
            elif ok =="n":
                correct = True
            elif ok == "quit":
                exit()
            else:
                print("Something went wrong!")
        #wenn alles durch ist save it
        clear()
        self.save_csv()
    
    #gehört zu change_item()    
    def change_status(self, entry="unbekannt"):
        clear()
        print(entry)
        print(f"\nAktueller Status: {entry['status']}")
        print("Auswahlmöglichkeiten:")
        for idx,val in enumerate(self.config["status__auswahl"]):
            print(idx,val)
        correct = False
        while not correct:
            user_index = input("\nWelchen Status möchtest du? quit/NR: ").lower()
            if user_index == "quit":
                exit()
            try: 
                user_index = int(user_index)
                user_value = self.config["status__auswahl"][user_index]
                correct = True
                
            except ValueError:
                print("Bitte eine Integer eingeben")
                continue
            except IndexError:
                print("Der Indexwert ist nicht vorhanden!")
                continue
        return user_value

    def delete_item(self):
        clear()
        print("DELETE Item")
        sleep(1)
        correct = False
        while not correct:
            sleep(1)
            print(self.csv_data)
            user_index = input("Welchen Datensatz möchtest du löschen? INT/quit: ").lower()
            if user_index == "quit":
                exit()
            try: 
                user_index = int(user_index)
                self.csv_data.drop([user_index], axis=0,inplace=True)
                
            except ValueError:
                print("Bitte eine INT eingeben! Sonst wird das nix mit uns\n")
                continue
            except KeyError: 
                print("Also in meiner Liste gibts den Index nicht ... !\n") 
                continue
            user_choice = input("Noch mehr löschen? (y/n/quit): ").lower()
            if user_choice == "y": 
                continue
            elif user_choice =="quit": 
                exit()
            else:
                correct = True
        self.save_csv()
    
    def print_csv(self):
        clear()
        print(self.csv_data)

    def search_by_index(self):
        clear()
        print("Search by INDEX")
        correct = False
        while not correct:
            sleep(1)
            print(self.csv_data)
            user_index = input("Welchen Index möchtest du Aufrufen? (INT/quit): ").lower()
            if user_index == "quit":
                exit()
            try: 
                user_index = int(user_index)
                clear()
                print(self.csv_data.loc[user_index])
            except ValueError:
                print("Eine INT ....")
                continue
            except KeyError:
                print("Eintrag nicht verfügbar!")
                continue
            
            user_choice = input("Weitere Einträge Aufrufen? (y/n/quit): ").lower()
            if user_choice == "quit":
                exit()
            elif user_choice =="n":
                correct = True
    
    def sort_after(self):
        keys = [item for item in self.csv_data.keys()]
        correct = False
        while not correct: 
            clear()
            print("Nach was soll sortiert werden?\n")
            for key in keys:
                print(str(keys.index(key)).rjust(2), key)
            user_index = input("Eingabe (INT/quit) ").lower()
            if user_index == "quit":
                exit()
            try: 
                user_index = int(user_index)
                print(self.csv_data.sort_values(by=[keys[user_index]]))
                correct = True
            except ValueError:
                clear()
                print("Bitte eine INT eingeben")
                sleep(2)
                continue
            except IndexError:
                clear()
                print("Index nicht verfügbar")
                sleep(2)
                continue
    
    def status_filter(self):
        correct = False
        while not correct: 
            clear()
            print("Filter for status:\n")
            for item in self.config["status__auswahl"]:
                print(str(self.config["status__auswahl"].index(item)).rjust(2), item)
            user_index = input("Eingabe (INT/quit) ").lower()
            if user_index == "quit":
                exit()
            try: 
                user_index = int(user_index)
                print(self.csv_data.loc[self.csv_data["status"].str.contains(self.config["status__auswahl"][user_index], case=False)])
                correct = True
            except ValueError:
                clear()
                print("Bitte eine INT eingeben")
                sleep(2)
                continue
            except IndexError:
                clear()
                print("Index nicht verfügbar")
                sleep(2)
                continue
            
    def save_csv(self):
        clear()
        self.csv_data = self.csv_data.sort_values(by=["firma"])
        self.csv_data.to_csv(self.config["csv_data"], index=False,sep=self.config["sep"])
        print(self.csv_data)
        print("\nDatensatz wurde gespeichert")