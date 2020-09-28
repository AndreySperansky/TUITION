def recursion (a, b): # основное условие задачи
	# Базовый случай
	if a == b:
		return str(a)
	if a > b:
	# Шаг рекурсии / рекурсивное условие
		return str(a) + " " + str(recursion(a - 1 , b))
	else:
	# Шаг рекурсии / рекурсивное условие
		return str(a) + " " + str(recursion(a + 1 , b))
	
print(recursion(20 , 15))         # если a > b  выводим по убыванию
print(recursion(10 , 15))         # если a < b  выводим по возрастанию