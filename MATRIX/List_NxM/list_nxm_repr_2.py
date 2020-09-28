my_array1 = [[1, 2, 3],  [2, 3, 4],  [3, 4, 5]]
my_array2 = [[4, 5, 6],  [5, 6, 7],  [6, 7, 8]]

def turn_matrix1(two_dim_list):
	return '\n'.join(['\t'.join([str(j) for j in i]) for i in two_dim_list])



def turn_matrix2(two_dim_list):
	matrix = []
	for i in two_dim_list:
		matrix.append([j for j in i])
	return matrix


m1 = turn_matrix1(my_array1)
print(m1, '\n')

m2 = turn_matrix2(my_array2)
print(m2, '\n')