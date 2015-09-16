#Bash Befehl *openpdf* zum Öffnen von Text-Datei im Pdf-Viewer

## Textdatei öffnen

Der Befehl zum Öffnen der Textdatei lautet:

    $ gedit test.md

oder Textdatei im Hintergrund öffnen

    $ gedit test.md &

Textdatei kann bearbeitet werden. Danach speichern und/oder schließen.

## Überprüfen, wie Text tatsächlich aussieht, durch öffnen von PDF

Der Befehl um die pdf-Datei zu aktualisieren und zu öffnen lautet:

    $ bash openpdf

oder pdf im Hintergrund öffnen

    $ bash openpdf &

### Erstellung des Scripts "openpdf"

Befehl wird aus zwei Befehlen zusammen gesetzt.

* 1. Übertragen von test.md in pdf-file


    $ echo "pandoc -o test.pdf test.md
    
* 2. Öffnen der pdf-file mit evince (pdf-viewer)
    
    $ evince test.pdf

Ganzer Befehl wird in Datei *openpdf* geschrieben. Zweiter Befehl muss nicht gepipet werden und kann in Zeile darunter geschrieben werden.

    $  echo "pandoc -o test.pdf test.md" > openpdf | echo "evince test.pdf" >> openpdf

Inhalt von Datei *openpdf* sieht dann folgendermaßen aus:                           

pandoc -o test.pdf test.md                                                          
evince test.pdf

mittlere Überschrift (erstellt durch Bindestriche in Zeile darunter)
--------------------------------------------------------------------

dickere Überschrift (erstellt durch Gleichheitszeichen in Zeile darunter)
=================================

### Überschrift mit Rauten davor

> die erste Zeile
> 
> die zweite Zeile (">" zwischen erster und zweiter Zeile)
> 
> ## Ein Blockquote

#### Phrase empahsis

some of these words *are emphasized*
some of these words _are emphasized also_.

