def fibo(n:int):
    print("Функция была вызвана с n= " + str(n))
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        #print("Функция была вызвана с n = " + str(n))
        res1 = fibo(n-1)
        print("Промежуточный результат для ", n, " равен res1 = ", res1)
        res2 = fibo(n-2)
        print("Промежуточный результат для ", n, " равен res2 = ", res2)
        res = res1 + res2
        print("Промежуточный результат для ", n, " равен res = ", res)
        return res

num = int(input("Введите целое число: "))
f = []
for i in range(num):
    f.append(fibo(i))
print(f)
print("Фибоначи %d равен: " % num, fibo(num))


