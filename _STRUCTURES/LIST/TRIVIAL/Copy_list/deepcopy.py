import copy

a = [1, 2, [1, 2]]

b = copy.deepcopy(a)
b[2][1]  = 200

# Список а не изменился
print(a)
# [1, 2, [1, 2]]
print(b)
# [1, 2, [1, 200]]