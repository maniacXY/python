# BEWERBUNGSDOC

## Dokumentation für Bewerbungen


Minimalistisches Consolenprogramm mit pandas und CSV

**MenuClass.py** ausführen und los gehts

Hier kannst du deine Bewerbungen einfach speichern, bearbeiten und abrufen. 
Das Programm basiert nur auf einer CSV-Datei und kann somit einfach in Excel oder LibreCalc importiert werden.

## Momentaner Stand

Auf Linux Ubuntu getestet
Python-Script momentan nur fehlerfrei ausführbar wenn man sich im selben verzeichnis befindet (chmod 600) reicht aus. 

Um es vom Terminal überall aufrufen zu können habe ich mir mit einer bash-alias beholfen

`alias MYALIAS="cd ~/SCRIPT/MenuClass.py && python3 MenuClass.py"`


## Bevor es los geht

**erste Eigene .csv**
- die Daten in der .csv können gelöscht werden -> WICHTIG! Erste Zeile muss so bestehen bleiben
- verwende einen bereits vorhandenen Datensatz
- allerdings funktioniert es nur sauber mit dem Header von der gegebenen csv (1.Zeile von data.csv)
- wenn du eine eigene .csv exportiert muss oder seperator ";" sein oder in den config geändert werden

**config ändern**

- am besten im jsonCONFIGdumper.py die configs anpassen und einmal ausführen, dann schreibt er in config.json
- config.json ändern (unübersichtlicher :P )
- die Namen der Menus können geändert werden, sollten sich aber in der Anzahl/Reihenfolge nicht ändern
- csv_data -> hier kannst du den Pfad deiner DATA.csv festlegen 
	- WICHTG: Falls ein anderer Speicherort muss DATA.csv bereits angelegt sein mit dem HEADER (sonst gibt es einen BUG und er kann die Datei nicht einlesen)
- sep -> falls deine CSV einen anderen Seperator hat (HIER default ";")
- status_auswahl -> hier kannst du deine eigenen Status hinterlegen, diese sollten dann auch in deiner .csv unter Status auftauchen oder können ggf mit dem Programm noch geändert werden

**VIEL SPASS**

