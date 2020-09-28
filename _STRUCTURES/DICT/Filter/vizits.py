lst = [
		{'visit1': ['Москва', 'Россия']},
		{'visit2': ['Дели', 'Индия']},
		{'visit3': ['Владимир', 'Россия']},
		{'visit4': ['Лиссабон', 'Португалия']},
		{'visit5': ['Париж', 'Франция']},
		{'visit6': ['Лиссабон', 'Португалия']},
		{'visit7': ['Тула', 'Россия']},
		{'visit8': ['Тула', 'Россия']},
		{'visit9': ['Курск', 'Россия']},
		{'visit10': ['Архангельск', 'Россия']},
]



def sort_list(list_value, param):
	res = []
	for d in list_value:
		for value in d.values():
			if value[1] == param:
				res.append(d)
	return res

rez = sort_list(lst, "Россия")
print(rez, '\n')

for d in rez:
	print(d)





res = [d for d in lst for value in d.values() if value[1] == 'Россия']
print(res, '\n')

