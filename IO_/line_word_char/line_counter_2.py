with open('my_file.txt', "r", encoding="utf-8") as myfile:
	count = sum(1 for line in myfile)

print(count)

with open('my_file.txt', encoding="utf-8") as myfile:
	count1 = sum(1 for line in myfile if line.rstrip('\n'))
	# str.rstrip('!')  возвращает копию строки str,  с конца которой устранены указанные символы

print(count1)

lst = ['l', 'i', 's', 't', '!', 3, 4, 5]

count3 = sum(1 for elm in lst)      # Суммирует по единичке для каждого элемента в списке
print(count3)