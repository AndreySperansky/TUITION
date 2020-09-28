"""!"""
"""Это функция, создающая итератор для формирования бесконечного цикла набора значения."""

from itertools import cycle


c = 0
for el in cycle( "ABC" ):
    if c > 10 :
        break
    print(el)
    c += 1