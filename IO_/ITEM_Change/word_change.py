test1 = ['One', 'Two', 'Three', 'Four']
test2 = ['Один', 'Два', 'Три', 'Четыре']


def Params(old_data, new_data, file1, file2):
	f1 = open(file1, 'r', encoding="UTF-8")
	text = f1.read()
	f1.close()
	f2 = open(file2, 'w', encoding="UTF-8")
	for word_number in range(len(old_data)):
		text = text.replace(old_data[word_number],
							new_data[word_number])

	f2.write(text)
	f2.close()

#f2 = open('myfile_out.txt', 'w', encoding="UTF-8")

Params(test1, test2, 'myfile_in.txt', 'myfile_out.txt')

#f2.close()