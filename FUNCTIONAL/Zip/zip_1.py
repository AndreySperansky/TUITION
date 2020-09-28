a = [1, 2, 3]
b = "xyz"
c = (None, True)

res = list(zip(a, b, c))
print(res)

#[(1, 'x', None), (2, 'y', True)]