L = [1, 2]
L.extend([3,4,5])                       # Добавление нескольких элементов в конец списка
print(L, '\n')
# [1, 2, 3, 4, 5]


lst = [1,2,3]
lst = lst + [4]
lst = lst + [L.pop()]
print("Новый список: ", lst, '\n')

# Новый список:  [1, 2, 3, 4, 5]