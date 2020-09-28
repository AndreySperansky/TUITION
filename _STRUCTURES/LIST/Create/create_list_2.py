lst = input("Введите числа через пробел: \n").split()
print(lst)
# ['1', '2', '3', '4', '5', '6', '7']

for i in range(len(lst)):
   lst[i] = int(lst[i])
print(lst)
# [1, 2, 3, 4, 5, 6, 7]

# Или что то же самое

b = list(map(int, input("Введите числа через пробел: \n").split()))
print(b, '\n')
# [1, 2, 3, 4, 5, 6, 7]
