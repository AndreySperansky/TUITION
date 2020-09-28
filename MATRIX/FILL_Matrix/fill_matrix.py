""""""
"""Ввод данных по одному через ENTER"""

ROW = int(input('Enter count of rows: '))
CLMN = int(input('Enter count of columns: '))


matrix = [[0] * CLMN for n in range(ROW)]




for i in range(ROW):
	for j in range(CLMN):
		matrix[i][j] = int(input(f'Введите элемент [{i}][{j}] : \n'))
		#print(matrix)
print(matrix)


for i in matrix:
	for j in i:
		print("%3d" % j, end = '')
	print()
	
# Enter count of rows: 3
# Enter count of columns: 3
# Введите элемент [0][0] :
# 1
# Введите элемент [0][1] :
# 2
# Введите элемент [0][2] :
# 3
# Введите элемент [1][0] :
# 2
# Введите элемент [1][1] :
# 3
# Введите элемент [1][2] :
# 4
# Введите элемент [2][0] :
# 3
# Введите элемент [2][1] :
# 4
# Введите элемент [2][2] :
# 5
# [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
#   1  2  3
#   2  3  4
#   3  4  5
