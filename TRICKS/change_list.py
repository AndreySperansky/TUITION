numbers = [1,2,3]

def change_number_in_list(input_list):
	input_list[1] = 200

# после вызова функции
change_number_in_list(numbers)
# список в основной программе тоже изменится
print(numbers)
