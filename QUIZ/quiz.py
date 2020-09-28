def f(sum, l=[]):
	l.append(sum)
	print(l)

l = [1]
f(10)       # [10]
f(10)       # [10, 10]
f(10, l)    # [1, 10]
f(10)       # [10, 10, 10]
print(l)    # [1, 10]
