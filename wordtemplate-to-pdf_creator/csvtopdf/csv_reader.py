import csv
import os
from datetime import datetime, timedelta
from pprint import pprint

class CSV_Reader:
    
    buggyRows = {}
    Berichtsnummer = 0
    
    
    def __init__(self, name = "Patrick Wiebell", path ="raw_data/", kurs = "IT-S-21.02", startBerichtnummer = 10) -> None:
        self.name = name 
        self.path = self.checkPath(path)
        self.kurs = kurs
        self.Berichtsnummer = startBerichtnummer

    def checkPath(self, path):
        if path[-1] != "/":
            return path + "/"
        else:
            return path
        

# takes a file and returns a dataDict 
    def readFile (self, file):
        dataDict = {}
        rowCount = 0
        with open(self.path + file, newline='',encoding="latin-1") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            #reader = csv.DictReader(csvfile, delimiter=";", header=None)
            for row in reader: 
                # row0 = Name of the Day
                if len(row) > 1:
                    if row[0] not in dataDict:
                        dataDict[row[0]] = []
                    # row1 = Data from Day 
                    #output = row[1].replace(",", ";")
                    output = row[1]
                    dataDict[row[0]].append(output)
                else:
                    self.buggyRows["row" + str(rowCount)] = row
                    rowCount += 1
        return dataDict

    def printBugs(self):
        print("Buggie Rows: ", self.buggyRows)

    def readFolder(self):
        files = os.listdir(self.path)
        berichte = []
        try:
            for file in files:
                # generete entries
                berichtData = self.readFile(file)
                # generate header
                headerData = self.namingReportHeader(file)
                # fuse these guys
                fusedData = {**headerData, **berichtData}
                berichte.append(fusedData)
        except Exception as e :
            print(e)
            print(file)
        pprint(berichte)
        
    def namingReportHeader(self, fileName):
        header = {
            "Tätigkeitsnachweis" : 10,
            "Kalenderwoche" : 10,
            "Monat" : 12,
            "Ausbildungsjahr" : 2022,
            "sign_date": "28.03.22",
            "date": 220323,
        }
        # 0 = 220711, 1 = 28 (Kalenderwoche), 2 = Berichtsheft.txt
        splitFile = fileName.split("_")
        header["sign_date"] = splitFile[0]
        header["Kalenderwoche"] = splitFile[1]
        
        # convert into datetime format
        dateFormat =  datetime.strptime(splitFile[0], '%y%m%d')
        #print(str(dateFormat.month).zfill(2))
        header["Tätigkeitsnachweis"] = self.Berichtsnummer
        self.Berichtsnummer += 1
        header["Monat"] = str(dateFormat.month).zfill(2)
        header["Ausbildungsjahr"] = dateFormat.strftime("%Y")
        header["date"] = dateFormat.strftime("%y%m%d")
        signDate = dateFormat + timedelta(days=5)
        header["sign_date"] = signDate.strftime("%d.%m.%y")

        return header
        # return a dict with all header data
        

