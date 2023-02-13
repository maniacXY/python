from mypdf_creator.MyCreator import Creator
from wordtojson.WordToJson import WordConverter
from csvtopdf.csv_reader import CSV_Reader
import os

INPUTPATH = "raw_data"
OUTPUTPATH = "pdf_data"
BERICHTSHEFTSTART = 28

def get_collection(wordfolder):
    mofu = f"{wordfolder}/"
    dateien = os.listdir(mofu)
    for datei in dateien:
        a = WordConverter(dirtodata=mofu, document=datei)
    return a

def main():
    userinput = int(input("Word oder CSV?\n1 : word\n2 : csv\n"))
    if userinput == 1:
        a = get_collection(INPUTPATH)
        for entry in a.main_dict["Berichte"]:
            output = "{}/{}_xKW{}_Berichtsheft.pdf".format(OUTPUTPATH,entry["date"], entry["Kalenderwoche"])
            Creator(data=entry, output=output)
    elif userinput == 2: 
        csvreader = CSV_Reader(startBerichtnummer=BERICHTSHEFTSTART)
        berichteDict = csvreader.readFolder()
        for entry in berichteDict:
            output = "{}/{}_xKW{}_Berichtsheft.pdf".format(OUTPUTPATH,entry["date"], entry["Kalenderwoche"])
            Creator(data=entry, output=output)

    else: 
        print("Option nicht vorhanden!")

if __name__ == "__main__":
    print("WORD/CSV TO PDF CONVERTER\n")
    print("Breche das Programm mit 'x' ab")
    print("Packe alle .docx/.csv Dateien in den Ordner 'raw_data'")
    start = input(f"\nBerichtsheft startet bei {BERICHTSHEFTSTART} korrekt?(y/n)")
    if start == "n":
        changeIt = int(input("Gib die Startnummer ein"))
        BERICHTSHEFTSTART = changeIt 
    
    user = input("Erstelle, falls nicht vorhanden den Ordner 'pdf_data' und bestätige mit y: ").lower()
    if user == "y":
        main()
        print("\nErstellung erfolgreich. Viel Spaß mit den PDF's :D")