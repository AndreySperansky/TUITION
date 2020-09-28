my_array1 = [[1, 2, 3],  [2, 3, 4],  [3, 4, 5]]
my_array2 = [[4, 5, 6],  [5, 6, 7],  [6, 7, 8]]



def turn_matrix1(lst):
	return "\n".join(' '.join(map(str, row)) for row in lst)

def turn_matrix2(lst):
	for row in lst:
		for elem in row:
			print(elem, end = ' ')
		print()
	print('\n')

m1 = turn_matrix1(my_array1)
print(m1, '\n')

# 1 2 3
# 2 3 4
# 3 4 5

m2 = turn_matrix2(my_array2)

# 4 5 6
# 5 6 7
# 6 7 8
