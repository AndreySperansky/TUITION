"""!"""
""" Заполнение матрицы случайными числами"""

from random import randint

row = int(input('Введите число строк матрицы: '))
col = int(input('Введите число столбцов матрицы: '))
A = []
# A - это матрица, кот. заполняеся строками [[1,2,3],[2,3,4],[4,5,6]....[n,l,m]]

for i in range(row):
    b = []
    # b - это строка матирцы [n,l, .... k]
    for j in range(col):
        b.append(randint(1, 10))
        print(f"{b[j]:4d}", end = '')
    A.append(b)                     # Заполненная строка добавляется в матрицу
    print()
    

# for i in A:
#     for j in i:
#         print("%3d" % j, end = '')
#     print()

#or

# for i in range(row):
#     for j in range(col):
#         print("%3d" % a[i][j], end = '')
#     print()

# Введите число строк матрицы: 4
# Введите число столбцов матрицы: 3
#   10   4   3
#    5   2   1
#    9   7   7
#    6  10  10