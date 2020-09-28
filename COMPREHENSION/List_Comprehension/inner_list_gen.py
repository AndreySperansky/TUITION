my_lst =[[0 for j in range(4)] for i in range(4)]
print(my_lst)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

"""Но если число 0 заменить на некоторое выражение, зависящее от i (номер строки) и j (номер столбца), 
то можно получить список, заполненный по некоторой формуле."""

my_lst1 =[[i * j for j in range(5)] for i in range(6)]

print(my_lst1)
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16], [0, 5, 10, 15, 20]]