"""Вычислить сумму случайного трехзначного чила"""

from random import random
n = random() * 900 + 100
n = int(n)
s = str(n)
a = int(s[0])
b = int(s[1])
c = int(s[2])

print("сумма случайного трехзначного чила:  ", a+b+c)


