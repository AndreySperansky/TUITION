"""Функция map может быть так же применена для нескольких списков, в таком случае
функция-аргумент должна принимать количество аргументов, соответствующее количеству списков:"""

l1 = [1, 2, 3]
l2 = [4, 5, 6]

new_list = list(map(lambda x, y: x + y, l1, l2))
print(new_list)

# [5, 7, 9]

"""Если же количество элементов в списках совпадать не будет, то выполнение закончится на минимальном списке:"""

l1 = [1, 2, 3]
l2 = [4, 5]

new_list = list(map(lambda x, y: + y, l1, l2))

print(new_list)
# [5, 7]