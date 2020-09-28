D = {'spam':1, 'eggs':3, 'toast':5}             # традиционное литеральное выражение
print(D)
# {'spam': 1, 'eggs': 3, 'toast': 5}
print(len(D))                      # Число элементов словаря
# 3
print('ham' in D)                  # Проверка на вхождение
# False
print(list(D.keys()))              # Создает новый список ключей
# ['spam', 'eggs', 'toast']
print(list(D.values()))            # Создает новый список значений
# [1, 3, 5]
print(list(D.items()))              # Создает новый список элементов словаря
# [('spam', 1), ('eggs', 3), ('toast', 5)]
print(D.setdefault("color", "gray",))   # Если ключа нет то он создается
#gray
print(D.setdefault("toast", 3,))   # Если ключ есть то просто возвращает значение по ключу
#5
print(D.get('spam'))                # Ключ присутствует в словаре
# 1
print(D.get('ham'))                 # Ключ отсутствует в словаре
# None
print(D.get('toast', 88))           # Ключ присутствует в словаре
#5
print(D.get('pizza', 88))           # Ключ отсутствует в словаре
#88
print(D['spam'])
# 1
print(D['pizza'])
# KeyError: 'pizza'
print(D)
# {'spam': 1, 'eggs': 3, 'toast': 5, 'color': 'gray'}