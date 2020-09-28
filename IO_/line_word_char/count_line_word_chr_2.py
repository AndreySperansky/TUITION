foo = open('my_file.txt', "r", encoding="utf-8")
line = 0
for i in foo:
	line += 1

	flag = 0
	word = 0
	for j in i:
		if j != ' ' and flag == 0:
			word += 1
			flag = 1
		elif j == ' ':
			flag = 0

	print(i, len(i), 'симв.', word, 'сл.')

print(line, 'стр.')
foo.close()