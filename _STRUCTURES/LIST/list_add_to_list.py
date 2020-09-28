a = ['a','b','c']
l = ['d','e','f']

a.extend(l)
# ['a', 'b', 'c', 'd', 'e', 'f']

print(a)

un = []
a = ['a','b','c']
b = ['d','e','f']
c = ['g','h','i']

un.append(a)
un.append(b)
un.append(c)
print(un)

# [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]