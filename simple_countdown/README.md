# Warum?
Ich hatte keinen Timer auf meinem Linux Rechner und dachte ich baue mir selber ein.

## OS
Getestet auf Ubuntu 20.04.4 LTS ob es auf Windows läuft weiß ich nicht, allerdings gibt es dort ja auch einen Countdown

## ToDo
Im Script muss oben der Pfad in `SCRIPT_DIR` und der `NAME_OF_SOUND` ergänzt werden.

Der Timer Name kann unter `NAME_OF_TIMER` geändert werden

Sound kann nach eigenen vorlieben getauscht werden. Sollte aber eine MP3 sein. 

Anschließend habe ich die .bashrc mit einer alias ergänzt

`alias timer="python3 /PATH/TO/DIR/timer.py"`

## Aufruf

Nachdem die alias erstellt ist kann das Script mit `timer` (oder deine Wunschalias) aufgerufen werden.

Standardzeit sind 10 Sekunden (kann ggf in line 15 `x="10"` geändert werden)

`timer` -> Countdown 10 Sekunden
`timer 20` -> Countdown 20 Sekunden
`timer 1:30` -> Countdown 1 Minute 30 Sekunden (bitte auf die Syntax achten)