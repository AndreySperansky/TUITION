# Программа Python для демонстрации вложенного тернарного оператора

a, b = 10, 20

print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")

# Вышеуказанный подход можно записать так:

# Программа Python для демонстрации вложенного тернарного оператора

a, b = 10, 20

if a != b:
	if a > b:
		print("a is greater than b")
	else:
		print("b is greater than a")
else:
	print("Both a and b are equal")