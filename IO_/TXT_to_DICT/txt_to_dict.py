d = {}
with open("data.txt", encoding="UTF-8") as file:
	for line in file:
		key, *value = line.split()
		d[key] = value

print(d)