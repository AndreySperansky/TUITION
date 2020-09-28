from random import randint

# Создание списка,
# его сортировка по возрастанию
# и вывод на экран

n = int(input("Введите длинну массива: "))
a = []
for i in range(n):
    a.append(randint(1, 100))
a.sort()
print(a)

# искомое число
value = int(input("Введите искомое число: "))

mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print("ID =", mid)