

lst = [1, 2, 3]
dct = {'a': 4, 'b': 5}
# print(apply(max, lst))    # Устаревшая функция
print(max(*lst))
print(list(lst))

# apply(dict, [], dct)  # Устаревшая функция
print(dict(**dct))

