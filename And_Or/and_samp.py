import math

if 1 > 2 and math.sqrt(-1):
	print("Ошибки не будет так как первое условие - ложь")
print('Двигаемся дальше')

# if math.sqrt(-1) and 1 > 2:
# 	print('Если поменять местами то будет ошибка')


# Первая ложь
print([1] and [] and '' and 1)

# Последняя истина
print([1] and 1 and 20 and 1.1)