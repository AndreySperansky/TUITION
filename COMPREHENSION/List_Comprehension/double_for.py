a = [(i, j) for i in 'abc' for j in [1, 2, 3]]
print(a)

# [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]

a = [i*j for i in [2,3,4,5] for j in [1, 2, 3,] if i*j > 5]
print(a)


# # [6, 6, 9, 8, 12, 10, 15]