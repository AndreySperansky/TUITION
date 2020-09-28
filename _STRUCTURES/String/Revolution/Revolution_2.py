for elem in reversed('TURBO'):
    print(elem)

"""получаем обратный итератор, который можно использовать
 цикличного перемещения элементов строки в обратном порядке:"""

text = ''.join(reversed('TURBO'))
print(text)

# 'OBRUT'

"""Метод join на первый взгляд может показаться немного странным. Так как он
является строковым методом (а не методом списка), он вызывается через указание
желаемой строки-разделителя."""


print('\n================================')

def reverse_string2(s):
    return "".join(reversed(s))

data = reverse_string2('TURBO')
print(data)

# 'OBRUT'

print('\n===========Считаем производительность=============')

import timeit
s = 'abcdefghijklmnopqrstuvwxyz' * 2
print(timeit.repeat(lambda: reverse_string2(s)))    # Средняя производительность