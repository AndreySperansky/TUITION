# Python 3.6, and beyond
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sorted_income = {k: incomes[k] for k in sorted(incomes)}
print(sorted_income)
#{'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}