data = [[1, 2, 3], [4, 5, 6]]

for _ in range(len(data)):
    data += data.pop(0)
print(data)

# [1, 2, 3, 4, 5, 6]