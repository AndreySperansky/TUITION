"""Сколько пятибуквенных слов можно составить из myset, A, B, L, E
наичинающихся и заканчивающихся согласной буквой и содержащих ровно 2 гласные
Каждая из допустимых букв может входить несколько раз"""


for b1 in 'table':
	for b2 in 'table':
		for b3 in 'table':
			for b4 in 'table':
				for b5 in 'table':
					rez = b1+b2+b3+b4+b5
					if rez[0] in 'tbl' and rez[-1] in 'tbl':
						if rez.count('a') + rez.count('e') == 2:
							print(rez)

