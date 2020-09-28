from string import printable
print(printable)
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
digit = '0123456789'

for b1 in digit:
	for b2 in digit:
		for b3 in digit:
			print(b1,b2,b3)

# 0 0 0
# 0 0 1
# 0 0 2
# 0 0 3
# 0 0 4
# 0 0 5
# 0 0 6
# 0 0 7
# 0 0 8
# 0 0 9
# 0 1 0
# 0 1 1
# 0 1 2
# ...