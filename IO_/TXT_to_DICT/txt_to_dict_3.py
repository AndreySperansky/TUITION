incoms = {}

with open("wagelist.txt", encoding="UTF-8") as file:
	for line in file:
		key, value = line.split()
		incoms[key] = int(value)



person = len(incoms)		# число работающих
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
