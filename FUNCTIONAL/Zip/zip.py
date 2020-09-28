keys = ['a', 'b', 'c']
vals = [1, 2, 3]
zipped = dict(zip(keys, vals))
zipped2 = list(zip(keys, vals))
zipped3 = tuple(zip(keys, vals))
print(zipped)
print(zipped2)
print(zipped3)


# {'a': 1, 'b': 2, 'c': 3}
# [('a', 1), ('b', 2), ('c', 3)]
# (('a', 1), ('b', 2), ('c', 3))



