"""3. Распаковывание последовательностей при неизвестном числе элементов"""

seq = [1, 2, 3, 4]
*a, b, c = seq
print(a, b, c)
a, *b, c = seq
print(a, b, c)
a, b, *c = seq
print(a, b, c)
a, b, c, *d = seq
print(a, b, c, d)
a, b, c, d, *e = seq
print(a, b, c, d, e)


# [1, 2] 3 4
# 1 [2, 3] 4
# 1 2 [3, 4]
# 1 2 3 [4]
# 1 2 3 4 []


for (a, *b, c) in [(1, 2, 3), (4, 5, 6, 7)]:
    print(a, b, c)

# 1 [2] 3
# 4 [5, 6] 7