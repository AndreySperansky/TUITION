input = [{1: 2}, {2: 2}, {1: 3}, {2: 1}, {1: 3}]

res = {}
for d in input:

# (assumes just one key/value per dict)
    (x, y), = d.items()
    res.setdefault(x, []).append(y)

print([{k: v} for (k, v) in res.items()])

# Результат:

# [{1: [2, 3, 3]}, {2: [2, 1]}]
# [обновление]
'''
 просто любопытно:
Можете ли вы объяснить, что происходит в

((x, y),) = d.items()

и

res.setdefault(x, []).append(y)#

Сначала ((x, y),) = d.items():

в этот момент d будет элементом из input, например {1: 2}
d.items() будет чем-то аналогичным [(1, 2)]
чтобы распаковать 1 и 2 в x и y, нам нужен дополнительный ',' (иначе интерпретатор будет считать,
что внешняя скобка делает группировку вместо определения одного кортежа элементов).

  res.setdefault(x, []).append(y)

res.setdefault(x, []).append(y) аналогичен:
if not res.has_key(x):
     res[x] = []
res[x].append(y)


'''
