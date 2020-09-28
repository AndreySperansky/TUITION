"""7. Удаление дубликатов в списке"""

items = [2, 2, 3, 3, 1]
print(list(set(items)))
# [1, 2, 3]


items = [2, 2, 3, 3, 1]

from collections import OrderedDict
print(list(OrderedDict.fromkeys(items).keys()))
# [2, 3, 1]