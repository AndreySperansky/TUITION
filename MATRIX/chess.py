"""Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
В левом верхнем углу должна стоять точка."""

n, m = [int(i) for i in input('Введите число строк и столбцов "n,m": \n').split(",")]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))