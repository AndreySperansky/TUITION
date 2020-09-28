def bin(n):
	"""Цифры двоичного представления двоичного числа"""
	if n == 0:
		return []
	n, d = divmod(n, 2)
	return bin(n) + [d]

num = input("Введите целое число: \n")
num = int(num)
print(bin(num))


#print(divmod(10, 3))