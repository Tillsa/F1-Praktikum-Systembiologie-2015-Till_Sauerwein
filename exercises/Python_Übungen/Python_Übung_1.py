#gff-file in Spalten aufteilen und Chromosomennummer sowie Startposition printen

gff_file_handle = open("gencode.v23.annotation_SHORT.gff3")

for current_line in gff_file_handle.readlines():# geht Zeile für Zeile durch die angegebene(geöffnete Datei) und führt die nachfolgenden Befehle für jede Zeile einzeln aus
	if current_line.startswith("#"):
		continue# bricht den Vorgang ab und macht mit der nächsten Zeile weiter
	columns_of_row = current_line.split()# Teilt alle Zeilen anhand von Leerzeichen oder Tabs auf
	print(columns_of_row[0], columns_of_row[1]) # schreibt Inhalt von Spalte 1 und 2 nebeneinander
	print("Chromosomennummer:",columns_of_row[0],"Start:",columns_of_row[3])# schreibt "Chromoso..." und dann die 1. Spalte, sowie "Start" und dann die 4.Zeile
	print("Chromosomennummer:{}Start:{}".format(columns_of_row[0], columns_of_row[1]))


