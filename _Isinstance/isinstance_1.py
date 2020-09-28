sumStr = ''
sumList = []
sumNum = 0
a = [5, 3, 'hello ', [3,4], 'world ', [5], 10.5]
for i in a:
	if isinstance(i, str):
		sumStr = sumStr + i
	elif isinstance(i, list):
		sumList = sumList + i
	elif isinstance(i, (int, float)):
		sumNum = sumNum + i

print(sumStr)
print(sumList)
print(sumNum)

# hello world
# [3, 4, 5]
# 18.5
