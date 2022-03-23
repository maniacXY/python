from mypdf_creator.MyCreator import Creator
from wordtojson.WordToJson import WordConverter
import os

INPUTPATH = "raw_data"
OUTPUTPATH = "pdf_data"

def get_collection(wordfolder):
    mofu = f"{wordfolder}/"
    dateien = os.listdir(mofu)
    for datei in dateien:
        a = WordConverter(dirtodata=mofu, document=datei)
    return a

def main():
    a = get_collection(INPUTPATH)
    for entry in a.main_dict["Berichte"]:
        output = "{}/{}_xKW{}_Berichtsheft.pdf".format(OUTPUTPATH,entry["date"], entry["Kalenderwoche"])
        Creator(data=entry, output=output)

if __name__ == "__main__":
    print("WORD TO PDF CONVERTER\n")
    print("Breche das Programm mit 'x' ab")
    print("Packe alle .docx Dateien in den Ordner 'raw_data'")
    user = input("Erstelle, falls nicht vorhanden den Ordner 'pdf_data' und bestätige mit y: ").lower()
    if user == "y":
        main()
        print("\nErstellung erfolgreich. Viel Spaß mit den PDFS :D")