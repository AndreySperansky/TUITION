D = {'spam':1, 'eggs':3, 'toast':5}             # традиционное литеральное выражение
print(D)

D['ham'] = ['grill', 'bake', 'fry']
print(D)

del D['eggs']                       # Удаление элемента по ключу
print(D)

D['brunch'] = 'Bacon'               # Добавление нового элемента
print(D)

print('\n ====конктенция (объединение) ===')

print(D)
D2 = {'toast':4, 'muffin':5}
D.update(D2)
print(D)

print('\n ====удаление элементов словаря по ключу===')
#
print(D)
D.pop('muffin')
D.pop('toast')              # Удаляет и возвращает значение заданного ключа
print(D)