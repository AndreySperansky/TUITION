mylst = ['2', '4', '3', '5', '1',]

result = [int(item) for item in mylst]

# result = list(map(int, array))


sumlist = sum(result)

print(result)
# [2, 4, 3, 5, 1]
print(sumlist)
# 15

result_array = []
for elem in mylst:
    result_array.append(int(elem))
array = result_array

print(array)
# [2, 4, 3, 5, 1]