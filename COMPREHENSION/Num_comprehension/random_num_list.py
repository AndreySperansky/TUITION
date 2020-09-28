from random import *


lst_len = 10

array = [randint(1,99) for i in range(lst_len)]
# array = [random.randrange(n1, n2) for i in range(lst_len)]

# Если без генератора
# array = []
# for i in range(lst_len):
#     array.append(randint(1,99))

for i in array:
    print(i, end = ' ')

print("\n", array)

array.sort()
print ('Элементы отсортированы по возрастанию')
print (array)