"""Сортировка по значениям"""
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
def by_value(item):
	return item[1]

for k, v in sorted(incomes.items(), key=by_value):
	print(k, '->', v)

#('orange', '->', 3500.0)
#('banana', '->', 5000.0)
#('apple', '->', 5600.0)

# можно совсем коротко
for value in sorted(incomes.values()):
	print(value)