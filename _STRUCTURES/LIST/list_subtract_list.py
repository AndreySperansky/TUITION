"""Удалить из списка а элементы списка b"""

a = [1, 2, 3, 4, 5]
b = [2, 3]

res = set(a) - set(b)
print(res)
print([res])
print(list(res), '\n')
# res = list(a) - list(b)   # class list  не поддерживает операциюю __sub__ '-'

# {1, 4, 5}
# [{1, 4, 5}]
# [1, 4, 5]

"""Но !!! способ работает не правильно в следующем случае"""

a = [1, 1, 1, 1, 2, 3, 4, 5]
b = [2, 3]

res = set(a) - set(b)
print(list(res), '\n')

# [1, 4, 5]

"""И этот способ работает не правильно в следующем случае"""

a = [1, 1, 1, 1, 2, 3, 4, 5]
b = [2, 3]


for number in a:
	if number in b:
		a.remove(number)
print(a)

# [1, 1, 1, 1, 3, 4, 5]

"""Правильный способ обход по копии списка"""

a = [1, 1, 1, 1, 2, 3, 4, 5]
b = [2, 3]


for number in a[:]:
	if number in b:
		a.remove(number)
print(a)
