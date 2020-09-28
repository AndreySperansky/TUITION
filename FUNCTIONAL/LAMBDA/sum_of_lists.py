l1 = [1, 2, 3]
l2 = [4, 5, 6]

new_list = list(map(lambda x, y: x + y, l1, l2))
print(new_list)

# [5, 7, 9]