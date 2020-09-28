with open('bytes.txt', 'wb',) as f:
	f.write(b'Hello, Bytes!')

# Открываем файл в текстовом режиме с указанием кодировки
with open('bytes.txt', 'r', encoding = 'ascii') as f:
	print(f.read())


with open('bytes.txt', 'wb',) as f:
	str = "Привет мир"
	f.write(str.encode('utf-8'))

with open('bytes.txt', 'r', encoding = 'utf-8') as f:
	print(f.read())

