my_array1 = [[1, 2, 3],  [2, 3, 4],  [3, 4, 5]]
my_array2 = [[4, 5, 6],  [5, 6, 7],  [6, 7, 8]]

class  Matrix(object):
	def __init__(self, two_dim_list):
		self.two_dim_list = two_dim_list

	def __str__(self):
		return "\n".join(' '.join(map(str, row)) for row in self.two_dim_list)

# def turn_matrix(self):
		# for row in self.two_dim_list:
		# 	for elem in row:
		# 		print(elem, end = ' ')
		# 	print()
		# print('\n')

m1 = Matrix(my_array1)
print(m1)
#m1.turn_matrix()

m2 = Matrix(my_array2)
print(m2)
#m2.turn_matrix()
