
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
#  Это - list comprehension
total_income = sum([value for value in incomes.values()])
print(total_income)

#14100.0

#Это выражение-генератор (generator expression)
total_income = sum(value for value in incomes.values())
print(total_income)

total_income = sum(incomes.values())
print(total_income)