"""Определить уникалные элементы списка"""

numbers = [1, 1, 2, 3, 3, 4, 4, 4, 5, 1, 2, 7,]

result = []
for number in numbers:
	if numbers.count(number) == 1:
		result.append(number)
print(result)

# [5, 7]