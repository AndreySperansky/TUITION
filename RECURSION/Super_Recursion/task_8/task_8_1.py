"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

try:
	NUM_COUNT = int(input("Сколько будет чисел? "))
	DIGIT = int(input("Какую цифру считать? "))
	while DIGIT > 9:
		print('Нужно вводить только одну цифру')
		DIGIT = int(input("Какую цифру считать? "))
	COUNT = 0
	for i in range(1, NUM_COUNT + 1):
		num = int(input(f"Число  {str(i)}: "))
		while num > 0:
			if num % 10 == DIGIT:
				COUNT += 1
			num = num // 10
	print(f"Было введено {COUNT} цифр {DIGIT}")

except ValueError:
	print('Ошибка, вы ввели строку!')
