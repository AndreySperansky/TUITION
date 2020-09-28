from random import *

import random

n = 10
array = []

for i in range(n):
    array.append(randint(1,99))

for i in array:
    print(i, end = ' ')

print('\n', array)


random.shuffle(array)
print(array)

B = sorted(array, key=lambda i: random.random())
print(B)