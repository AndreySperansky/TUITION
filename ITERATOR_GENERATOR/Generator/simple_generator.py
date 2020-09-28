def counter(low, high, step):
	current = low
	while current <= high:
		yield  current
		current += step

for c in counter(3, 9, 2):
	print(c, end = " ")

# 3 5 7 9