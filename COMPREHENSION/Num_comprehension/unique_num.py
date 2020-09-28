"""Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. 
Для выполнения задания обязательно использовать генератор."""

lst = [1, 2, 7, 4, 9, 5, 6, 2, 5, 2, 9, 3, 3,]
print(f"Первоначальный список: {lst}  \n ")
# Первоначальный список: [1, 2, 7, 4, 9, 5, 6, 2, 5, 2, 9, 3, 3]

used = []
unique = [used.append(x) for x in lst if x not in used ]
print(f'unique {unique}')
print(f'used {used}')
# unique [None, None, None, None, None, None, None, None]
# used [1, 2, 7, 4, 9, 5, 6, 3]

unique = [x for x in lst if x not in used and used.append(x)]   # == x not in used and None
print(f'unique {unique}')
print(f'used {used}')
# unique []
# used [1, 2, 7, 4, 9, 5, 6, 3]

used = set()
unique2 = [x for x in lst if x not in used and (used.add(x) or True)]
print(f'unique2 {unique2}')
print(f'used {used}')
# unique2 [1, 2, 7, 4, 9, 5, 6, 3]
# used {1, 2, 3, 4, 5, 6, 7, 9}


# конструкция x and y  возвращает x если х False  и не выполняет y,  в противном случае переходит к y и возвращает его
# Если x отсутствует в used (то есть True) выполняется конструкция and (used.add(x) or True)]
# Конструкция х or y  возвращает х если х True и не выполняет y, в противном случае переходит к y и возвращает его
# конструкция (used.add(x)) всегда возвращает None, то есть мы переходим к условию OR  и мы получаем True
#  В результате у нас выполняется и used.add(x)  и при этом мы получаем True

unique3 = [x for i, x in enumerate(lst) if i == lst.index(x)]
print(f'unique3 {unique3}')
# unique3 [1, 2, 7, 4, 9, 5, 6, 3]

from functools import reduce
unique4 = reduce(lambda l, x: l.append(x) or l if x not in l else l, lst, [])
# Присоединить х к l и вернуть это l  когда х  не в l.  (Благодоря OR .append оценивается и после этого возвращается l)
# Вернуть l нетронутым если х  в l.
print(f'unique4 {unique4}')
# unique4 [1, 2, 7, 4, 9, 5, 6, 3]


unique5 = reduce(lambda l, x: l+[x] if x not in l else l, lst, [])
print(f'unique5 {unique5}')
# unique5 [1, 2, 7, 4, 9, 5, 6, 3]


from collections import Counter
counter = Counter(lst)
print(counter, '\n') # Подсчитываем количество повторений для каждого числа
# Counter({2: 3, 9: 2, 5: 2, 3: 2, 1: 1, 7: 1, 4: 1, 6: 1})

unique6 = list(counter)
print(f'unique6 {unique6}')
# unique6 [1, 2, 7, 4, 9, 5, 6, 3]

single = [x for x,n in counter.items() if n==1]
print(single)

# [1, 7, 4, 6]
