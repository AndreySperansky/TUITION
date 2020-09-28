"""выводит последовательность чисел ФФибоначи не превышающих n"""


def fib(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, (a + b)
    return

fib(100)
