lst =	[
	('a', 1),
	('a', 2),
	('a', 3),
	('b', 1),
	('b', 2),
	('c', 1),
	]

dic = {}
for x, y in lst:
    dic.setdefault(x, []).append(y)
print(dic)

# {'a': [1, 2, 3], 'b': [1, 2], 'c': [1]}