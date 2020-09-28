"""Итеральное исчисление факториала работает быстрее рекурсивного"""

def iterative_factorial(n):
    if n == 0 or n==1:
        res = 1
        return res
    else:
        res = 1
        for i in range(2, n+1):
            res = res * i
        return res

num = abs(int(input("Введите целое число: ")))
print("Факториал числа %d равен: " % num, iterative_factorial(num))