def factorial(n):
    print("Функция была вызвана с n= " + str(n))
    if n == 0 or n==1:
        return 1
    else:
        res = n * factorial(n - 1)
        print("Промежуточный результат для ", n, " * factorial(" , n-1, "): ",res)
        return res

num = abs(int(input("Введите целое число: ")))
print(factorial(num))

