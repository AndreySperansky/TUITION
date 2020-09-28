incoms = {'Иванов:': 50000,
		'Петров:': 15000,
		'Сидоров:': 25000,
		'Волков:': 10000,
		'Зайцев:': 45000,
		'Пушкин:': 75000
		}

person = len(incoms)		# можно и так определить число работающих
print(f"Количество работников получивших зарплату: {person} человек")
#print(incoms)

total_income = sum(incoms.values())
avg_incom = total_income / person
#print(total_income)

print(f"Средний доход, полученный на одного работника: {round(avg_incom, 2)}")
low_incom = {x:y for x,y in incoms.items() if y <= 20000}
#print(low_incom)


print("Сотрудники получившие доход менее 20000: \n")
for key in low_incom:
	print(key, " -- > ",  low_incom[key])


