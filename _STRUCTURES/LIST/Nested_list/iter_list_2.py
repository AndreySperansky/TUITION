from functools import reduce

def line_tree(lst = None ):
	ls = lst or []
	res = []
	for x in ls: # Обход элементов одного уровня
		if not isinstance(x, list):
			#res += [x] # Элементы дополняются в список непосредственно
			res.append(x)
		else:
			res += line_tree(x)  # Списки обрабатываются рекурсивными вызовами
	return res

lis = [['define', ['if', '1', ['*', 'n', 1, ['fac', ]]]]]

print(line_tree(lis), '\n')


"""ТО ЖЕ САМОЕ В ФУНКЦИОНАЛЬНОМ СТИЛЕ СТИЛЕ"""

f = lambda ls: reduce(lambda res, x: res+[x] if not isinstance(x, list) else res + f(x), ls, [])

ls = [['define', ['if', '1', ['*', 'n', ['fac', ]]]]]
print(f(ls))

# ['define', 'if', '1', '*', 'n', 'fac']

