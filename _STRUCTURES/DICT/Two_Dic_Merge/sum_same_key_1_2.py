adic = (
      {'Петя': 6, 'Вася': 8, 'Дима': 11, 'Юля': 3},
      {'Петя': 5, 'Вася': 36, 'Дима': 4, 'Юля': 8},
      {'Петя': 54, 'Вася': 21, 'Дима': 22, 'Юля': 39},
      {'Петя': 61, 'Вася': 48, 'Дима': 71, 'Юля': 73}
    )

res = {}
for dic in adic:                                     # пробегаем по списку словарей
  for key in dic:                               # пробегаем по ключам словаря
    try:
      res.setdefault(key, []).append(dic[key])
    except KeyError:                                    # если ключа еще нет - создаем
      res[key] = dic[key]

print(res)

# {'Петя': [6, 5, 54, 61], 'Вася': [8, 36, 21, 48], 'Дима': [11, 4, 22, 71], 'Юля': [3, 8, 39, 73]}