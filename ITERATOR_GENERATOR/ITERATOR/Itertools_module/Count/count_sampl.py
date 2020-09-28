"""!"""
"""Это итератор, возвращающий равномерно распределенные переменные начиная с числа, переданного как
стартовый параметр. Также допустимо указание значения шага."""

from itertools import count

for el in count( 7 ):
    if el > 15 :
        break
    else :
        print(el)