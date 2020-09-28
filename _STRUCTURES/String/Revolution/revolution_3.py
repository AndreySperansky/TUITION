# CLASSIC

def reverse_string3(s):
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)

data = reverse_string3('TURBO')
print(data)

# 'OBRUT'

"""Метод join на первый взгляд может показаться немного странным. Так как он
является строковым методом (а не методом списка), он вызывается через ука-
зание желаемой строки-разделителя."""


print('\n===========Считаем производительность=============')

import timeit
s = 'abcdefghijklmnopqrstuvwxyz' * 2
print(timeit.repeat(lambda: reverse_string3(s)))    # Самый непроизводительный метод