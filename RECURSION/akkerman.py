"""Функция аккермaнa"""

from sys import getrecursionlimit, setrecursionlimit

# setrecursionlimit(1001)
print(getrecursionlimit())

# 1000


def recursion (m, n):
	# Базовый случай
	if m == 0 :
		return n + 1
	# Шаг рекурсии / рекурсивное условие
	elif n == 0 and m > 0:
		return recursion(m - 1 , 1 )
	# Шаг рекурсии / рекурсивное условие
	else :
		return recursion(m - 1 , recursion(m, n - 1 ))
	
print(recursion( 0 , 2 ))
print(recursion(2, 0))

# 3
# 3