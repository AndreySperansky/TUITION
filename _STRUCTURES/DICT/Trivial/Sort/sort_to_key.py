import operator
#
dic = {3: 'three', 1: 'one', 2:'two'}

sorted_dic = sorted(dic.items(), key = operator.itemgetter(0))
print(sorted_dic)

# [(1, 'one'), (2, 'two'), (3, 'three')]