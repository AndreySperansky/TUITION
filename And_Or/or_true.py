# Добавление элемента в список

# Классический способ

def add_to_list(input_list = None):
	if input_list is None:
		input_list = []
	input_list.append(2)
	return input_list

result = add_to_list([0,1])
print(result)
result = add_to_list()
print(result)

# Через OR

def add_to_list(input_list = None):
	#  используем свойство or  вместо условие
	input_list = input_list or []
	input_list.append(2)
	return input_list

result = add_to_list([0,1])
print(result)
result = add_to_list()
print(result)
