from math import sqrt, ceil

# def primes(num):
#     *a, = range(num)
#     a[4::2] = [0] * (num // 2 - 2)
#     for i in range(3, ceil(sqrt(num)), 2):
#         # начиная  i^2  с шагом i  зануляем элементы
#         a[i * i::i] = [0] * len(a[i * i::i])
#         # схлопываем нули и выдаем числа начиная с 2
#     return sorted(set(a))[2:]

def primes(num):
    *a, = range(num)    #  распаковка range в кортеж из одного элемента
    print(a)
    a[4::2] = [0] * (num // 2 - 2 )  # исключаем четные
    print(a)
    for i in range(3, ceil(sqrt(num)), 2):  # цикл по нечетным с 3 до корня из n
        a[i * i::i] = [0] * len(a[i * i::i])     # зануляем кратные i^2
    print(a)
    return sorted(set(a))[2:]   # убираем 0, сортируем, выводим

print(primes(40))


# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]