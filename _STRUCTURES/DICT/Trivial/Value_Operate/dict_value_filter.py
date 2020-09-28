a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {}  # Create a new empty dictionary
for key, value in a_dict.items():
# If value satisfies the condition, then store it in new_dict
	if value <= 3:
		new_dict[key] = value

print(new_dict)

#{'one': 1, 'two': 2}