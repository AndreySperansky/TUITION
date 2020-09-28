def gensquares(n):
    for i in range(n):
        yield i**2           # Позднее продолжить работу с этого места


for i in gensquares(5):     #Возобновить работу функции
    print(i, end = ':')     #Вывести последнее полученное значение
# 0:1:4:9:16:

x = gensquares(4)

print("\n")
print(next(x))
# 0
print(next(x))
# 1
print(list(x))
# [4, 9]

print(list(x))
# []