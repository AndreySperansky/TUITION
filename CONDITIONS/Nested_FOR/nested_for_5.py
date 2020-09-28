for i in range(3):
	for j in range(5):
		print('*', end = '')
	print('')

# *****
# *****
# *****

for i in range(3):
	for j in range(5):
		print(i, end = '')
	print()

# 00000
# 11111
# 22222

for i in range(3):
	for j in range(5):
		print(j, end = '')
	print()

# 01234
# 01234
# 01234

for i in range(10):
	for j in range(i):
		print(j, end = '')
	print()
#
# 0
# 01
# 012
# 0123
# 01234
# 012345
# 0123456
# 01234567
# 012345678

for i in range(1, 10):
	for j in range(1, i+1):
		print(j, end = '')
	print()

# 1
# 12
# 123
# 1234
# 12345
# 123456
# 1234567
# 12345678
# 123456789