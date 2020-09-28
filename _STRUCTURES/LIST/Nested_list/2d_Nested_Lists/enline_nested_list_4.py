from functools import reduce
from operator import add
data = [[1, 2, 3], [4, 5, 6]]
nova = reduce(add, data)
print(nova)

# [1, 2, 3, 4, 5, 6]

