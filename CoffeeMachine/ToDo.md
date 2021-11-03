# Was brauche ich für Funtionen?

## 1. keep track of ressources
Ressourcen müssen ausgegeben werden + tracken 

## 2. transfrom what uve got
alle Optionen aus "MENU" in einen String packen
Ausgabe:; ```Zur Verfügung steht (Option1/2/3)```

## 3. User input
Userabfrage was er will Auswahlliste wird von Punkt 2 erzeugt

## 4. Funktion genug ressource übrig?
Ist genug Ressource verfügbar um Getränk X auszugeben?
- ja -> True
- nein -> False

## 5. Funktion Geldeinwurf mit Preis
hat user genug Geld eingeworfen?
- ja -> True
- nein -> False

## 6. User input in Funktion final check
ressourcenoutput + geldoutput muss übergeben werden
1. Ressource True? (Punkt 4)
   1. ja -> nächster Check
   2. nein > Ausgabe "Ressourcen fehlen"
2. Geld True? (Punkt 5)
   1. ja -> Produkt ausgabe
   2. nein -> Aussage "zu wenig Kohe"