from random import *
n = 10
array = []

for i in range(n):
    array.append(randint(1,99))

for i in array:
    print(i, end = ' ')

print("\n", array)