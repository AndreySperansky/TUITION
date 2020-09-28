"""Переворот с помощью среза"""

def reverse_string1(s):
    return s[::-1]

print(reverse_string1('TURBO'))

# 'OBRUT'

print('\n===========Считаем производительность=============')

import timeit
s = 'abcdefghijklmnopqrstuvwxyz' * 2
print(timeit.repeat(lambda: reverse_string1(s)))    # Самый производительный метод