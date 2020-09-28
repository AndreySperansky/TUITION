

adic = [
		{"A": "VA1", "B": "VB1", "C": "VC1"},
		{"A": "VA2", "B": "VB2", "C": "VC2"},
        {"A": "VA3", "B": "VB3", "C": "VC3"},
		]

dic = {}
for k in adic[0]:
	dic[k] = [d[k] for d in adic]

print(dic)
# {'A': ['VA1', 'VA2', 'VA3'], 'B': ['VB1', 'VB2', 'VB3'], 'C': ['VC1', 'VC2', 'VC3']}

# Работает только в случае совпадения ключей во всех словарях
dic1 = {k: [d[k] for d in adic] for k in adic[0]}           # dictionary comprehension
print(dic1)
# {'A': ['VA1', 'VA2', 'VA3'], 'B': ['VB1', 'VB2', 'VB3'], 'C': ['VC1', 'VC2', 'VC3']}

# dic1 = dict((k, [d[k] for d in dictList]) for k in dictList[0])   # как вариант

print(adic[0])