import math

numbers = [4, 1, 2, 3, -4, -2, 7, 16]

# Создать список из чисел котрые имеют квадратный корень меньше 2 [1,2,3]

result = []
# Обычный способ

for number in numbers:
	if number > 0:
		sqrt = math.sqrt(number)
		#  квадратный корень менше 2
		if sqrt < 2:
			result.append(number)

print(result)

result = []
# Через линивый and

for number in numbers:
	if number > 0 and math.sqrt(number) < 2:
		result.append(number)
print(result)

# Через генератор

result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)
