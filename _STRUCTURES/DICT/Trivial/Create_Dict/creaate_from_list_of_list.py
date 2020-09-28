lst =	[
	['a', 1],
	['a', 2],
	['b', 3],
	['c', 4],
	['d', 5],
	['f', 6],
	]

dic = {}
for i in lst:
	dic[i[0]] = i[1]
print(dic)

# {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'f': 6}

dic = {}

for key, value in lst:
	dic.setdefault(key, []).append(value)
print(dic)
# {'a': [1, 2], 'b': [3], 'c': [4], 'd': [5], 'f': [6]}