import random   #подключаем модуль генератора
n1 = int(input('Введите нижнюю границу массива='))
n2 = int(input('Введите верхнюю границу массива='))
kolvo = int(input('Введите количество элементов массива= '))

if kolvo < 2:
    print ('Задано мало элементов')
else:

    a = [random.randrange(n1, n2) for i in range(kolvo)]
    a.sort()
    print ('Элементы отсортированы по возрастанию')
    print (a)
    a.sort(reverse=True)
    print ('Элементы отсортированы по убыванию')
    print (a)