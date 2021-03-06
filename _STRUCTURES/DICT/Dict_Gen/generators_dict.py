L=list(zip(['a', 'b', 'c'], [1, 2, 3]))     #Объединить ключи и значения
print(L)

D=dict(zip(['a', 'b', 'c'], [1, 2, 3]))     #Создать словарь из результата
print (D, '\n')
# {'a': 1, 'b': 2, 'c': 3}

#Генератор словаря 1:
D1 = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}       #Генератор словаря
print(D1, '\n')
# {'a': 1, 'b': 2, 'c': 3}

#Генератор словаря 2:
D2 = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D2, '\n')
# {1: 1, 2: 4, 3: 9, 4: 16}

#Генератор словаря 3:
D3 = {x: x ** 3 for x in range(1,5)}
print(D3, '\n')
# {1: 1, 2: 8, 3: 27, 4: 64}

#Генератор словаря 4:
D4 = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D4, '\n')
# {'spam': 'SPAM!', 'eggs': 'EGGS!', 'ham': 'HAM!'}

# Генератор словаря 5:
D5 = dict.fromkeys(['a', 'b', 'c'], 0) # Инициализация списком ключей
print(D5)
# {'a': 0, 'b': 0, 'c': 0}