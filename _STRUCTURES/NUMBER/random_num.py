"""Получить случайное целое и случайное вещественное число в заданном диапазоне"""
from random import randint
from random import random

print("Диапазон для целых чисел: ")
imin = int(input("Введите Min: "))
imax = int(input("Введите Max: "))
n = randint(imin, imax)
print("Cлучайное целое число %d" % n )

print("Диапазон для целых чисел: ")
fmin = float(input("Введите Min: "))
fmax = float(input("Введите Max: "))
f = random() * (fmax - fmin) + fmin
print("Cлучайное вещественное число % .3f" % f )