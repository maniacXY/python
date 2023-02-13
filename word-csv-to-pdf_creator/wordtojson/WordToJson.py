import docx2txt
from datetime import datetime, timedelta
import os
import json

class WordConverter:
    tage = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Für die Richtigkeit")
    main_dict = {
        "Name": "Your Name",
        "Ausbildungsgruppe": "Your Group",
        "Berichte":[]
    }
    
    def __init__(self, dirtodata, document, aenderung=False) -> None:
        self.document = document
        self.dirtodata= dirtodata
        self.aenderung = aenderung
        self.document_temp = f"{document.split('.')[0]}.txt"
        self.temp_data = self.word_to_temp()
        self.json_key = document.split("_")[0]
        self.my_dict = self.dictionary_creator(self.temp_data)
        self.save_it()
        
    def word_to_temp(self):
        """converts Data and pass it to put in in a dictionary"""
        #convert .docx to data
        text = docx2txt.process(f"{self.dirtodata}/{self.document}")
        #write it into the tempfile
        with open(self.document_temp, "w") as text_file:
            text_file.write(text)
        #read the data
        with open(self.document_temp, "r") as file: 
            data = file.readlines()
        os.remove(self.document_temp)
        #remove spaces, tabs and not needed stuff
        data = [item.strip() for item in data]
        data = [item for item in data if len(item) > 0]
        return data
        
    def dictionary_creator(self,temp_data):
        temp_dict = self.main_dict
        construct_date = self.document.split("_")[0]    #type STR
        construct_date_format = datetime.strptime(construct_date, "%y%m%d")
        sign_date = construct_date_format + timedelta(days=5)
        
        mydata_dict = {
            "Tätigkeitsnachweis":temp_data[temp_data.index("Tätigkeitsnachweis Nr.")+1],
            "Kalenderwoche": temp_data[temp_data.index("Kalenderwoche/Monat")+1].split("/")[0],
            "Monat": temp_data[temp_data.index("Kalenderwoche/Monat")+1].split("/")[1],
            "Ausbildungsjahr": temp_data[temp_data.index("Ausbildungsjahr")+1],
            "sign_date": sign_date.strftime("%d.%m.%y"),
            "date": int(construct_date)
        }
        for i in range(len(self.tage)-1):
            mydata_dict[self.tage[i]] = temp_data[temp_data.index(self.tage[i])+1:temp_data.index(self.tage[i+1])]
        temp_dict["Berichte"].append(mydata_dict) 
        return temp_dict
    
    def save_it(self):
        with open("berichte.json", "w") as d:
            json.dump(self.main_dict, d)