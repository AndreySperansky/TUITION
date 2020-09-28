person = {'name': 'Max', 'phones': [1234, 2345]}
with open('person.dat', 'wb') as f:
	# например запишем объект в файл построчно
	# сначала запишем имя
	name = person['name']
	# добавляем перенос строки, переведем в байты и запишем
	f.write(f'{name}\n'.encode('utf-8'))
	# пулчим телефоны
	phones = person['phones']
	# запишем 1 телефон в новую строку
	for phone in phones:
		f.write(f'{phone}\n'.encode('utf-8'))

print('объект записан')