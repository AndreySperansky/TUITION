"""Функция суммирует все что будет передано в качестве аргументов"""

def mysum(L= None):
    L=[] or L
    return 0 if not L else L[0] + mysum(L[1:])  # Трехместный оператор

print(mysum([1]))
#   1
print(mysum([1, 2, 3, 4, 5, 'a']))
#   15
