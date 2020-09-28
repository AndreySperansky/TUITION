import random

min_number = 1
max_number = 100
result = None
my_number = int(input("Загадайте число от 1 до 100: \n"))
print(my_number)

while result != '=':
	number = random.randint(min_number, max_number)
	if number < my_number:
		print(f"К: {number} < {my_number}")
	elif number > my_number:
		print(f"К: {number} > {my_number}")
	else:
		print(f"К: {number} = {my_number}")
	result = input("=<> \n")

	if result == '<':
		min_number = number + 1
	elif result == '>':
		max_number = number - 1
else:
	print("*********************")
	print("Компьютер победил!!!")
	print("*********************")