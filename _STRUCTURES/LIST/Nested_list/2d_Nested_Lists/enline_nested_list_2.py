import itertools
data = [[1, 2, 3], [4, 5, 6]]
nova = list(itertools.chain.from_iterable(data))
print(nova)

# [1, 2, 3, 4, 5, 6]
