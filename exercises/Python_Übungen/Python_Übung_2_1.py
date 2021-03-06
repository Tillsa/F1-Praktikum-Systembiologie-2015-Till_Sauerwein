# gff-file, header rausnehmen, nur gene betrachten, Chromosomennummer und Genlänge printen
gff_file_handle = open("gencode.v23.annotation_SHORT.gff3")

for current_line in gff_file_handle.readlines():# geht Zeile für Zeile durch die angegebene(geöffnete Datei) und führt die nachfolgenden Befehle für jede Zeile einzeln aus
	if current_line.startswith("#"):
		continue# bricht den Vorgang ab und macht mit der nächsten Zeile weiter	
		columns_of_row = current_line.split()
		if current_line[2].startswith("g"):
			gene_length = int(columns_of_row[4]) - int(columns_of_row[3])
			print("Chromosomennummer:{} Länge:{}".format(columns_of_row[0], gene_length))
