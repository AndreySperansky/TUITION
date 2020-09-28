# def my_filter(numbers):
# 	result = []
# 	for number in numbers:
# 		if number % 2 == 0:
# 			result.append(number)
# 	return result

""" Функции фильтрации списка чисел"""

def my_filter(numbers, function):
	result = []
	for number in numbers:
		if function(number):
			result.append(number)
	return result

def is_even(number):
	return number % 2 == 0


numbers = [1,2,3,4,5,6,7,8]

print(my_filter(numbers, is_even))

def is_odd(number):
	return number % 2 != 0

print(my_filter(numbers, is_odd))

def ultra_four(number):
	return number >= 4

print(my_filter(numbers,ultra_four))

# Lambda

print(my_filter(numbers, lambda number: number < 5))


# [2, 4, 6, 8]
# [1, 3, 5, 7]
# [4, 5, 6, 7, 8]
# [1, 2, 3, 4]


