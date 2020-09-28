# Подсчет слов в файле in_file.txt и запись результата в out_file.txt

with open('in_file.txt', "r") as f, open('out_file.txt', "w") as g:
	for line in f:
		if line == "\n":
			g.write("0\n")
		else:
			g.write(str(line.count(" ") + 1) + "\n")    # подсчитывает пробелы " "

