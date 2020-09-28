a = {

	'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
	'Lukov': {'age': 2002, 'hobby': 'bascetball', 'car': 'Opel'},
	'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
	'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
	'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
	'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
	'Elisev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
	'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
	'Bukov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
	'Gavrilov': {'age': 1980, 'hobby': 'soccer', 'car': 'Mercedes'},
	'Efremov': {'age': 2006, 'hobby': 'bascetball', 'car': 'BMW'},
}

b = [elem for elem in a]
print(b, '\n')
# ['Sidorov', 'Lukov', 'Petrov', 'Gorbachev', 'Kostin', 'Isaev', 'Elisev', 'Kozlov', 'Bukov', 'Gavrilov', 'Efremov']

b = [a[elem] for elem in a]
print(b, '\n')
# [{'age': 1995, 'hobby': 'soccer', 'car': 'BMW'}, {'age': 2002, 'hobby': 'bascetball', 'car': 'Opel'},
# {'age': 1991, 'hobby': 'chess', 'car': 'BMW'}, ...

b = [a[elem]['car'] for elem in a]
print(b, '\n')
# ['BMW', 'Opel', 'BMW', 'BMW', 'Audi', 'BMW', 'Audi', 'Opel', 'BMW', 'Mercedes', 'BMW']

b = [a[elem]['car'] for elem in a if a[elem]['age'] < 2000]
print(b, '\n')
# ['BMW', 'BMW', 'BMW', 'Audi', 'BMW', 'Mercedes']

b = [(elem, a[elem]['car']) for elem in a if a[elem]['age'] < 2000]
print(b, '\n')
# [('Sidorov', 'BMW'), ('Petrov', 'BMW'), ('Gorbachev', 'BMW'), ('Elisev', 'Audi'), ('Bukov', 'BMW'),
# ('Gavrilov', 'Mercedes')]

b = [(elem, a[elem]['car']) for elem in a if a[elem]['age'] < 2000 and a[elem]['hobby'] == 'soccer']
print(b, '\n')

# [('Sidorov', 'BMW'), ('Bukov', 'BMW'), ('Gavrilov', 'Mercedes')]
