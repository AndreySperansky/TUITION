# Глава 7 Луц М

print (int('64'), int('100', 8), int('40', 16), int('1000000', 2))

print (int('0x40', 16), int('0b1000000', 2)) # Допускается использовать литералы


print (eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))


print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))

print ('%o, %x, %X' % (64, 255, 255))


print ('\n')

import math
print (math.pi, math.e) # Распространенные константы

print (math.sin(2 * math.pi / 180)) # Синус, тангенс, косинус

print (math.sqrt(144), math.sqrt(2)) # Квадратный корень

print (pow(2, 4), 2 ** 4) # Возведение в степень

print (abs(-42.0), sum((1, 2, 3, 4))) # Абсолютное значение, сумма

print (min(3, 1, 2, 4), max(3, 1, 2, 4)) # Минимум, максимум


print ('\n')


import random

print (random.random())

print (random.randint(1, 10))

print (random.randint(1, 10))

print (random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))

print (random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))


print ('\n')



