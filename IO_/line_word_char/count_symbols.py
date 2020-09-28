# программа, читающая данные посимвольно и копирует их из файла input.txt в файл output.txt:

input = open(file = 'input.txt', mode = 'r', encoding="UTF-8")
output = open(file = 'output.txt', mode = 'w', encoding="UTF-8")
c = input.read(1)
while len(c) > 0:
	output.write(c)
	c = input.read()
input.close()
output.close()

print(c)