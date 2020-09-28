"""Вывести неповторяющиеся элементы массива"""
from random import randint

N = 20
NUMS = [0] * N

for i in range(N):
    NUMS[i] = randint(-5, 5)
    print(NUMS[i], end=' ')

print()

for i in range(N):
    f = True
    for j in range(N):
        if NUMS[i] == NUMS[j] and i != j:
            f = False
            break
    if f:
        print(NUMS[i], end=' ')