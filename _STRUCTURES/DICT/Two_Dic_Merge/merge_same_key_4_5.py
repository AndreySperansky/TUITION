import operator
from functools import reduce

adic = [
		{"A": "VA1", "B": "VB1", "C": "VC1"},
		{"A": "VA2", "B": "VB2", "C": "VC2"},
        {"A": "VA3", "B": "VB3", "D": "VC3"},
		]

# На случай если имеются разные ключи создаем массив ключей
allKeys = reduce(operator.or_, (set(d.keys()) for d in adic), set())
print(allKeys)

# {'C', 'D', 'B', 'A'}

# Затем нужно защититься от недостающих ключей в некоторый словарях
dic1 = {k: [d[k] for d in adic if k in d] for k in allKeys}           # dictionary comprehension
print(dic1)
# {'C': ['VC1', 'VC2'], 'D': ['VC3'], 'B': ['VB1', 'VB2', 'VB3'], 'A': ['VA1', 'VA2', 'VA3']}