numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Получить только четные числа

def is_even(number):
	return number % 2 == 0

result = filter(is_even, numbers)
print(result)

result = list(result)
print(result)


# Набор строк

names = ['Max', 'Alex', 'Rate',]

print(list(filter(lambda x: len(x) > 3, names)))
