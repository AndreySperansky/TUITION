date = '02.11.2019'
d, m, y = date.split('.')
print(d, m, y)

months = {
	'01': 'января',
	'02': 'февраля',
	'03': 'марта',
	'04': 'апреля',
	'05': 'мая',
	'06': 'июня',
	'07': 'июля',
	'08': 'августа',
	'09': 'сентября',
	'10': 'октября',
	'11': 'ноября',
	'12': 'декабря',
}

days = {
	'01': 'первое',
	'02': 'второе',
	'03': 'третье',
	'04': 'четвертое',
	'05': 'пятое',
	'06': 'шестое',
	'07': 'седьмое',
}

result = f'{days[d]} {months[m]} {y} года'
print(result)