from functools import reduce

f = lambda ls: reduce(lambda res, x: res+[x] if not isinstance(x, list) else res + f(x), ls, [ ])

ls = [['define', ['if', '1', ['*', 'n', ['fac', ]]]]]
print(f(ls))

#isinstance(x, list)  проверяет является ли x случаем (типом) списка или нет