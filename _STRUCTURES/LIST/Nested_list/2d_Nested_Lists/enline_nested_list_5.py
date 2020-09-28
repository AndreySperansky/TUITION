from itertools import chain
data = [[1, 2, 3], [4, 5, 6]]
nova = list(chain(*data))
print(nova)

# [1, 2, 3, 4, 5, 6]
