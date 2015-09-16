gff_file_handle = open("gencode.v23.annotation_SHORT.gff3")

for current_line in gff_file_handle.readlines():
	columns_of_row = current_line.split()
	if current_line.startswith("#"):
		continue
	if columns_of_row[2].startswith("g"):
		gene_length = int(columns_of_row[4]) - int(columns_of_row[3])
		print("Laenge:{}".format(gene_length))
