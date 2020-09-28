file = open("data.txt")
onstring = file.read().split("\n")[:-1]

""" Внимание! если после последней строки не будет символа переноса строки то она выпадет!"""

print(onstring)

dict = dict()

for item in onstring:
	key = item.split(" ")[0]
	value = item.split(" ")[1:]
	dict[key] = value

file.close()

print(dict)