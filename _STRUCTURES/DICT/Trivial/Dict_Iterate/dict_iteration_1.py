dic = {'one': 'один', 'two': 'два', 'three': 'три'}

for key, value in dic.items():
	print(key, '\t', value)

# one 	    один
# two 	    два
# three 	три

astr = ""
for key, value in dic.items():
	astr += ("{" if astr == "" else ", ") + f"\"{key}\": \"{value}\""
astr += "}"
print(astr, '\n')
# {"one": "один", "two": "два", "three": "три"}

for value in dic.values():
	print(value)

# один
# два
# три

for key in dic.keys():
	print(key)

# one
# two
# three