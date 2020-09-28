"""Двоичный (бинарный) поиск элемента в массиве"""
# [1, 3, 7, 8, 15, 16, 19, 20, 30, 32]


from random import random

N = 20
def srch(c, e):
    m = N // 2
    i = 0
    j = N - 1
    while c[m] != e and i <= j:
        if e > c[m]:
            i = m + 1
        else:
            j = m - 1
        m = (i + j) // 2
    if i > j:
        return 0
    else:
        return m + 1

p = 1
q = 4
a = [0] * N
for i in range(N):
    a[i] = int(random() * (q - p)) + p
    p += 3
    q += 3
    print(a[i], end=' ')
print()
e = int(input('Число: '))
i = srch(a, e)
if i == 0:
    print('Такого числа нет.')
else:
    print(f'Число находится на {i}-м месте.')
