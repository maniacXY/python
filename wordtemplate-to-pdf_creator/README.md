# FOR WHAT?
You put multiple documents with the format (look template ./raw_data)

Change it individually for you and get every document in a nice formatted .pdf in ./pdf_data

# Ordnerstruktur

- mypdf_creator
  - fonts
    - normal, bold, italic
  - ascii-header
  - sample sign.png
- pdf_data
  - *for the output*
- raw_data
  - *for the input .docx* -> look at the Template
- wordtojson
  - .py
  
# Config for mypdf_creator

## own header
change or remove './mypdf_creator/assciistandard.png'

change line 8 in MyCreator.py

## sign and name
Please dont change the fontsize or linehight or u crash the pdf format

You can add your own **sing** 
'./mypdf_creator/sample.png'

change line 31 

You can change *Arbeitsgruppe* in line 32 

You can add your name in line 33

## individual lines
You can change the naming of the lines, work through MyCreator.py and WordToJson.py (dont recommend tht )

# raw_data
Please use the template_document in ./raw_data.

You can change the data, copy multiple documents and put them all into the folder

pls take care of the naming DATE_KWXX_NAME.docx

# Config for wordtojson

## Naming
change line 9 -> your name

change line 10 -> your group

# main_word-to-pdf-converter.py

use default *INPUTPATH* line 5 or change it 

use default *OUTPUTPATH* line 5 or change it 

# Run main_word-to-pdf-converter.py

# Programmierungsdokumentation

## Aufbau von Json für Bericht
Strutkur von Json 
```json 
{
  "Name": "Your Name",
  "Ausbildungsgruppe": "Your Group",
  "Berichte": [
    {
      "Tätigkeitsnachweis": "01",
      "Kalenderwoche": "12",
      "Monat": "03",
      "Ausbildungsjahr": "2022",
      "sign_date": "28.03.22",
      "date": 220323,
      "Montag": [
        "Some data monday"
      ],
      "Dienstag": [
        "Some data tuesday"
      ],
      "Mittwoch": [
        "Some data wednesday",
        "Multiple lines = no Problem"
      ],
      "Donnerstag": [
        "Lorem ipsum"
      ],
      "Freitag": [
        "Bla bla"
      ]
    }
  ]
}
```

## Converter to PDF
Creator benötigt einen outputName mit dem Format wie die PDF heißen soll
Aufbau `220323_xKW12_Berichtsheft.pdf`

und ein Berichtseintrag siehe darüber

```python
from mypdf_creator.MyCreator import Creator
a = get_collection(INPUTPATH)
    for entry in a.main_dict["Berichte"]:
        output = "{}/{}_xKW{}_Berichtsheft.pdf".format(OUTPUTPATH,entry["date"], entry["Kalenderwoche"])
        Creator(data=entry, output=output)
```