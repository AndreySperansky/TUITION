x = [
	{'Car': 'Honda', 'id': 12},
	{'Car': 'Mazda', 'id': 45},
	{'Car': 'Toyota', 'id': 20}
	]
# Вариант1
desired_val = None
for item in x:
	if item['id'] == 20:
		desired_val = item
		break
print(desired_val)
# {'Car': 'Toyota', 'id': 20}

# Вариант2
foo = lambda x: next(i for i in x if i['id'] == 20)
print(foo(x))
# {'Car': 'Toyota', 'id': 20}

# Вариант3
val = next(filter(lambda x: x['id'] == 20, x))
print(val)
# {'Car': 'Toyota', 'id': 20}
