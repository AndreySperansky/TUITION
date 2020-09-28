
l1 = [2, 7, 5, 3]
l2 = [-2, 1, 0, 4]
temp = map(lambda x, y: x+y, l1, l2)
print(temp, '\n')
print(list(temp), '\n')

# [0, 8, 5, 7]


l1 = [2, 7, 5, 3]
l2 = [-2, 1, 0, 4]

temp1 = list(map(lambda x, y: {x: y}, l1, l2))
temp2 = list(map(lambda x, y: (x, y), l1, l2))
temp3 = list(map(lambda x, y: [x, y], l1, l2))

print(temp1)
print(temp2)
print(temp3, '\n')

# [{2: -2}, {7: 1}, {5: 0}, {3: 4}]
# [(2, -2), (7, 1), (5, 0), (3, 4)]
# [[2, -2], [7, 1], [5, 0], [3, 4]]


l1 = [2, 7, 5, 3]
l2 = [-2, 1, 0, 4]

temp1 = tuple(map(lambda x, y: {x: y}, l1, l2))
temp2 = set(map(lambda x, y: (x, y), l1, l2))
temp3 = list(map(lambda x, y: [x, y], l1, l2))

print(temp1)
print(temp2)
print(temp3)