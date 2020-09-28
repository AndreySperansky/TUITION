""".Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(string:str):
	print(((string[0].title(), string[1:]))if string else string)
	return ''.join((string[0].title(), string[1:]))if string else string
	# Соединяет первую букву [0] и остальную часть кортежа [1:]
	# Условие if string is string  нужно только для случая когда string == '' т.е. когда len(string) == 0
	#  и возникает ошибка "IndexError: string index out of range"

# Эквивалент данного кода в императивной (командной) парадигме:

	# if string :
	# 	return ''.join((string[0].title(), string[1:]))
	# else:
	# 	return string
		# pass


def user_temp(string: str):
	return ' '.join(map(int_func, string.split(' ')))
#
assert int_func('колбаса с сыром') == 'Колбаса с сыром', "int_func('колбаса с сыром')"
assert int_func('колбаса') == 'Колбаса', "int_func('колбаса')"
assert int_func('самса') == 'Самса', "int_func('самса')"
assert int_func('') == '', "int_func('')"
print(int_func('колбаса'))
print(int_func('колбаса с сыром'))
print(int_func(''))
print(3)

assert user_temp('колбаса с сыром') == 'Колбаса С Сыром', "user_temp('колбаса с сыром')"
assert user_temp('самса с ветчиной') == 'Самса С Ветчиной', "user_temp('самса с ветчиной')"
assert user_temp(' ') == ' ', "user_temp(' ')"

print(user_temp('колбаса с сыром'))
print(user_temp('самса с ветчиной'))
print(32)

print(len(''))