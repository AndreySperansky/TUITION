from functools import reduce

lst = range(10)
f = lambda x, y: (x[0] + y, x[1]+[x[0] + y])
temp = ( reduce(f, lst, (0, [])))

print(temp)