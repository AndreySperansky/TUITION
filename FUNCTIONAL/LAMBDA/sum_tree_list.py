from functools import reduce
"""" СУММИРОВАНИЕ ВЛОЖЕННЫХ СПИСКА """


f1 = lambda lst: reduce(lambda tot, x: tot + x  if not isinstance(x, list) else tot + f1(x),lst,0)
lst = [1, [2, [3, 4], 5], 6, [7, 8]]
lst2 = [[[[[1], 2], 3], 4], 5]
lst3 = [1, [2, [3, [4, [5]]]]]

print(f1(lst))
print(f1(lst2))
print(f1(lst3))


"""ТО ЖЕ САМОЕ В ПРОЦЕДУРНОМ СТИЛЕ"""

def sum_tree(L):
    tot = 0
    for x in L: # Обход элементов одного уровня
        if not isinstance(x, list):
            tot += x # Числа суммируются непосредственно
        else:
            tot += sum_tree(x) # Списки обрабатываются рекурсивными вызовами
    return tot

lst = [1, [2, [3, 4], 5], 6, [7, 8]] # Произвольная глубина вложения
print(sum_tree(lst)) # Выведет 36
# Патологические случаи
print(sum_tree([1, [2, [3, [4, [5]]]]])) # Выведет 15 (центр тяжести справа)
print(sum_tree([[[[[1], 2], 3], 4], 5])) # Выведет 15 (центр тяжести слева)

"""То же самое, только в функциоальном стиле"""



