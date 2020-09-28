"""Сортировка массива метдом пузырька -2  """
"""Реализация спомощью цикла  for"""

from random import randint

n = int(input("Введите длинну массива: "))
mas = []

for i in range(n):
    mas.append(randint(1,100))
print(mas)

print("   ")
for i in range(n - 1):
    for j in range(n - i - 1):
        if mas[j] > mas[j + 1]:
            temp = mas[j]
            mas[j] = mas[j + 1]
            mas[j+1] = temp

print(mas)

for j in mas:
    print(j, end = ' ')