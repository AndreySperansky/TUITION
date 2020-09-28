print(list(range(-5, 5)))  # Итератор в Python 3.0
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
print(filter((lambda x: x > 0), range(-5, 5)))  # Итератор в Python 3.0
# <filter object at 0x00FEBFF0>
print(list(filter((lambda x: x > 0), range(-5, 5))))  # Итератор в Python 3.0
# [1, 2, 3, 4]
