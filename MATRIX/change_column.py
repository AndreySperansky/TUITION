def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]


n, m = [int(i) for i in input('Введите число строк и столбцов "n,m": \n').split(",")]
a = [[int(j) for j in input(f'Заполните {i+1}-ю строку из {m} \
по {m} чисела через ",": \n').split()] for i in range(n)]
i, j = [int(i) for i in input(f'Введите номера столбцов i j которые нужно поменять через ",": \n').split(",")]
swap_columns(a, i, j)
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))