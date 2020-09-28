a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
	new_dict[value] = key

print(new_dict)

# {1: 'one', 2: 'two', 3: 'thee', 4: 'four'}