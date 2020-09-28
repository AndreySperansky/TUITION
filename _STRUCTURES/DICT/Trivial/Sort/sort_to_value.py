import operator

dic = {2: 'c', 3: 'b', 4: 'd', 1: 'a'}

sorted_dic = sorted(dic.items(), key = operator.itemgetter(1))
print(sorted_dic)

# [(1, 'a'), (3, 'b'), (2, 'c'), (4, 'd')]
