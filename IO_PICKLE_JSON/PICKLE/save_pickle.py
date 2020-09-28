import pickle

person = {'name': 'Max', 'phones': [1234, 2345]}

# откроем файл

with open('person.txt', 'wb') as f:
	# сразу  пишем объект целиком с поощью pickle
	pickle.dump(person, f)

print('Объект записан!')
