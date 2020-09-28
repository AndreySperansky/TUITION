import pickle

with open('person.txt', 'rb') as f:
	# сразу читаем из файла с помощью pickle
	person = pickle.load(f)

print(person)

