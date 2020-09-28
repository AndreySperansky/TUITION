a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 3}
print(new_dict)
# {'one': 1, 'two': 2, 'thee': 3}