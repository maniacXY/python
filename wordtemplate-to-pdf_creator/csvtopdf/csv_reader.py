import csv
import os
from pprint import pprint

class CSV_Reader:
    
    buggyRows = {}
    
    
    def __init__(self, name = "Patrick Wiebell", path ="raw_data/", kurs = "IT-S-21.02", startBerichtnummer = 10) -> None:
        self.name = name 
        self.path = self.checkPath(path)
        self.kurs = kurs
        self.startBerichtsnummer = startBerichtnummer

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
                    self.buggyRows["row" + rowCount] = row
                    rowCount += 1
        return dataDict

    def printBugs(self):
        print(self.buggyRows)

    def readFolder(self):
        files = os.listdir(self.path)
        try:
            for file in files:
                pprint(self.readFile(file))
                print(file)
        except Exception as e :
            print(e)
            print(file)
        
