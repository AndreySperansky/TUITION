"""6. Транспонирование двумерного массива данных"""


original = [('a', 'b'), ('c', 'd'), ('e', 'f')]
transposed = zip(*original)
print(list(transposed))

# [('a', 'c', 'e'), ('b', 'd', 'f')]