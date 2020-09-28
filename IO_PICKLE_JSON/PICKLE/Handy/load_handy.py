# читаем объект из файла

# откроем файл

with open('person.dat', 'rb') as f:
	# теперь нам надо знать как мы записывали объект
	# простаем файл в список
	result = f.readlines()

# теперь создаем исходный объект
person = {}
# Первый элемент это его имя
person['name'] = result[0].decode('utf-8').replace('\n', '')
# далее идут телеыоны
phones = []
for phone in result[1:]:
	phones.append(phone.decode('utf-8').replace('\n', ''))

person['phones'] = phones

# получили исходный объект, Это было достаточно тяжело. Ф что если что-то измениятся?
print(person)
