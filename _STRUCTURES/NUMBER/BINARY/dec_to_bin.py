n = int(input('Введите число: '))
b = ''
while n > 0:
	b = str(n % 2) + b
	n = n // 2

print(b)
# 110


A = bin(5)
print(A)
# '0b101'
B = bin(6)
print(B)

