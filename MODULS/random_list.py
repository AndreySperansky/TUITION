import random

"""
2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. 
Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
"""



def get_random(input_list):
	if input_list:     # То есть если лист не пустой
		result = random.choice(input_list)
		return result


if __name__ == '__main__':
	print(get_random([2, 3, 4, 5, 7]), '\n')

	print(get_random([]))






