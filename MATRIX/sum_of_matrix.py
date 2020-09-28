"""Задание заключается в том, чтобы для матрицы NxM, где N, M < 1000, просуммировать K (K < 100000)
наборов элементов, заключенных в прямоугольнике, углы которого задаются координатами (x1, x2, y1, y2)."""

"""
То есть для матрицы

1 2 3  
2 4 6  
7 8 9  
и координат (1, 2, 1, 3) это будет прямоугольник

1 2  
2 4  
7 8
"""

#sum( [ sum( arr[k][x1:x2] ) for k in range(y1,y2) ] )


a = [[1, 2, 3], [2, 4, 6], [7, 8, 9]] # для проверки
N, M = 3, 3 # для проверки

b = [[0 for j in range(M + 1)] for i in range(N + 1)]

for i in range(N):
    for j in range(M):
        b[i][j] = b[i-1][j] + b[i][j-1] - b[i-1][j-1] + a[i][j]

# для ответа на вопрос задачи - сумма чисел в прямоугольнике (x1, x2, y1, y2)
x1, x2, y1, y2 = 0, 2, 0, 1
result = b[x2][y2] - b[x1-1][y2] - b[x2][y1-1] + b[x1-1][y2-1]

print(result)