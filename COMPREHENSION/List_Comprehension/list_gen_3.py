''''''
'''Отсортировать  положительные числа'''

numbers = [1, 2, 3, 4, 5, -1, -2, -3]

result = []
for number in numbers:
	if number > 0:
		result.append(number)


print(result, '\n')

# Через функцию filter()

result = filter(lambda number: number > 0, numbers)
print(list(result), '\n')

# Через генератор

result =  [number for number in numbers if number > 0]
print(result, '\n')