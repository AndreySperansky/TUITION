"""Вычисление суммы всех элементов списка при помощи reduce:"""

from functools import reduce

items = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, items)

print(sum_all)

# 15