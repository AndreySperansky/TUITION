
def mysum(L):
    if not L: return 0
    return nonempty(L)      # Вызов функции, которая вызовет эту функцию
def nonempty(L):
    return L[0] + mysum(L[1:])   # Косвенная рекурсия

print(mysum([1.1, 2.2, 3.3, 4.4]))


#11