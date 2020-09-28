"""Сортировка массива метдом пузырька -3  """
"""Реализация спомощью цикла  while"""

from random import randint

n = int(input("Введите длинну массива: "))
a = []
for i in range(n):
    a.append(randint(1, 99))
print(a)

i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        j += 1
    i += 1

print(a)
