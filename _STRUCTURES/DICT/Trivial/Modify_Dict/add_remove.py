

d = {'x': 2, 'y': 12}

d.update(x = 5)
d.update({'w': 123})
d['lst'] = 1, 'el', 33
d['z'] = 77
d.setdefault("color", "gray",)       #Если ключа color нет добавит этот ключ вместе со значением в словарь
try:
	d['llst']

except KeyError as err:
	print("Проверьте ваши данные!", err, '\n')


print(d, '\n')
print(d.keys(), '\n')
print(d.values(), '\n')
print(d.items())

# {'x': 5, 'y': 12, 'w': 123, 'lst': (1, 'el', 33), 'z': 77, 'color': 'gray'}


del d['x']
d.pop('y')
d.popitem()     # удаляет произвольный элемент(не случайный)

print(d, '\n')
print(d.keys(), '\n')
print(d.values(), '\n')
print(d.items())
