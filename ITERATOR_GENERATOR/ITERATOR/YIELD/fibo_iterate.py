"""С ИСПОЛЬЗОВАНИЕМ ГЕНЕРАТОРА YIELD"""

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

num = int(input("Введите целое число: "))
data = list(fibonacci(num))
print(data)

