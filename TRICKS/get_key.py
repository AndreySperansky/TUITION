""" 10. Вывод значения по умолчанию для отсутствующего ключа словаря"""
d = {'a':1, 'b':2}

print(d.get('c'))
print(d.get('c', 3))

# None
# 3


class MyDict(dict):
    def __missing__(self, key):
        return key

D = MyDict(a=1, b=2)
print(D)
print(D['a'])
print(D['c'])

# {'a': 1, 'b': 2}
# 1
# c