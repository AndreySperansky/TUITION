D = {'spam':1, 'eggs':3, 'toast':5}                     # традиционное литеральное выражение
print(D)

rec = {}                                                # динамическое присвоение
rec['name'] = 'mel'
rec['age'] = 45
rec['job'] = 'trainer/writer'
print(rec['name'])
print(rec)

D2 = dict(name='mel', age=45)                           # Форма именованных аргументов
print(D2)

D3 = dict([(1, 'one'), (2, 'two'), (3, 'three')])       # Кортежи ключ/значение
print(D3)

dic = dict()                                             # Создание пустого словаря
dic[1] = 'one'
dic[2] = 'two'
dic[3] = 'three'
print(dic)

keyslist = [1, 2, 3, 4,]
valslist = ['one', 'two', 'three', 'four']

dic1 = dict(zip(keyslist, valslist))
print(dic1)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

dic2 = dict.fromkeys(['a', 'b', 'c', 'd'], 'letter')
print(dic2)
# {'a': 'letter', 'b': 'letter', 'c': 'letter', 'd': 'letter'}