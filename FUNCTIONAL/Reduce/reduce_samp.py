"""!!!"""
"""Функция reduce из переданного в него списка берет первые два элемента на первом проходе, 
выполняет для них некую функцию, сохраняет результат выполнения функции, берет следующий элемент списка и выполняет 
функцию для предыдущего результата и следующего элемента списка и т.д."""

from functools import reduce  # В 3.0 требуется выполнить импортирование

print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))
# 10
print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))

"""Что эквивалентно"""

L = [1, 2, 3, 4]
res = L[0]
for x in L[1:]:
    res = res + x

print(res)


# 10

def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally


print('\n')

print(myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5]))
# 15
print(myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5]))
# 120
