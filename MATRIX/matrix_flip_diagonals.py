"""Обмен значений главной и побочной диагоналей квадратной матрицы"""
#  у главной диагонали индексы i = j
#  у побочной i - индекс строки, инлекс столбца N - 1 - j


from random import random

N = 10
EXT_LST = []
for i in range(N):
    z = []
    for j in range(N):
        n = int(random() * 100)
        z.append(n)
        print(f"{n:4d}", end='')
    print()
    EXT_LST.append(z)
print()

for i in range(N):
    for j in range(N):
        if i == j:
            b = EXT_LST[i][j]
            EXT_LST[i][j] = EXT_LST[i][N - 1 - j]
            EXT_LST[i][N - 1 - j] = b

for i in range(N):
    for j in range(N):
        print(f"{EXT_LST[i][j]:4d}", end='')
    print()
