from random import *
n = 10
array = []

for i in range(n):
    array.append(randint(1,99))
# [49, 98, 71, 19, 94, 62, 10, 98, 76, 51]


print("\n", array)

for i in array:
    print(i, end = ' ')

# 49 98 71 19 94 62 10 98 76 51