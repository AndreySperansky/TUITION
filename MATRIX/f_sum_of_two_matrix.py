my_array1 = [[1, 2, 3],  [2, 3, 4],  [3, 4, 5]]
my_array2 = [[4, 5, 6],  [5, 6, 7],  [6, 7, 8]]

def matrix_sum(m1, m2):
	res_matrix = []
	res_row = []
	for i in range(len(m1)):
		for j in range(len(m1)):
			summa = m2[i][j] + m1[i][j]
			res_row.append(summa)
			if len(res_row) == len(m1):
				res_matrix.append(res_row)
				res_row = []                  # освобождаем строку для заполнения данными следующего ряда
	return res_matrix

res = matrix_sum(my_array2, my_array1)

print(res)