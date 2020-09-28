"""Сортировка массива метдом пузырька -4  """
"""Реализация спомощью функции"""

from random import randint


def bubble(array):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
    return array


n = int(input("Введите длинну массива: "))
a = []
for i in range(n):
    a.append(randint(1, 99))

print(a)
bubble(a)
print(a)