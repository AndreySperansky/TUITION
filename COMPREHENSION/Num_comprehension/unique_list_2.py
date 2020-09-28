my_list = [1, 2, 1, 3, 2, 4, 3, 5, 4, 3, 2, 3, 1]
unique_list = [ e   for i, e in enumerate(my_list)  if my_list.index(e) == i  ]
print(unique_list)
# [1, 2, 3, 4, 5]