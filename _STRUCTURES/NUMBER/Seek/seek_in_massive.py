from random import randint

n = 10
x = 5
mas = [randint(1, 10) for i in range(n)]
print(mas)
# [4, 1, 10, 2, 8, 1, 5, 2, 3, 10]
# num = -1 ???

for i in range(n):
	if mas[i] == x:
		print("mas[", i+1, "]=", x, sep = "")
		break

else:
	print("Не нашли!")

# mas[7]=5