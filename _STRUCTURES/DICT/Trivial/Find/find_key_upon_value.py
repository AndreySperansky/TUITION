dic = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'a'}

my_val = 'a'
my_list = ['b', 'd']
keys = []
keys1 = []

for key, value in dic.items():
	if value == my_val:
		keys.append(key)
print(keys)

# [1, 5]

for key, value in dic.items():
	if value in my_list:
		keys1.append(key)
print(keys1)

# [2, 4]