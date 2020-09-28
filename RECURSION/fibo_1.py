"""Числа Фибоначчи"""

def fib(n, sum):
	if n < 1:
		return sum
	return fib(n - 1, sum + n)

print(fib(7, 0))

# 28