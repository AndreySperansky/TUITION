import random

n = 3
m = 3

a = [ [random.randint(1, 10) for j in range(m)] for i in range(n)]
for i in a:
	print(i)

b = [a[i][j] for i in range(n) for j in range(m) if i == j]
print('main diagonal', b)

# Выводим вторую строку
c = [a[2][j] for j in range(m)]
print('2 stroka', c)

# [1, 10, 9]
# [7, 5, 3]
# [3, 1, 6]
# main diagonal [1, 5, 6]
# 2 stroka [3, 1, 6]