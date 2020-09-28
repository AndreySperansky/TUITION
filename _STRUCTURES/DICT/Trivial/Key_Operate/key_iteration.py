a_dict = {'color': 'blue',
		'fruit': 'apple',
		'pet': 'dog'}
keys = a_dict.keys()
print(keys, '\n')

#dict_keys(['color', 'fruit', 'pet'])

for key in a_dict.keys():
	print(key,)

print('\n')

for key in a_dict.keys():
	print(key, '->', a_dict[key])

print('\n')

for key in a_dict.keys():
	print(a_dict[key])