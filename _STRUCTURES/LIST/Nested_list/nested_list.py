a = [1, [4, [4, 5, [15]]], 2, [2, 3, 4, [5, 6, [7,8], 10, 11]]]

def rec(spisok, level = 1):
	print(*spisok, 'level=', level)
	for i in spisok:
		if type(i) == list:
			rec(i, level + 1)


rec(a)

# 1 [4, [4, 5, [15]]] 2 [2, 3, 4, [5, 6, [7, 8], 10, 11]] level= 1
# 4 [4, 5, [15]] level= 2
# 4 5 [15] level= 3
# 15 level= 4
# 2 3 4 [5, 6, [7, 8], 10, 11] level= 2
# 5 6 [7, 8] 10 11 level= 3
# 7 8 level= 4