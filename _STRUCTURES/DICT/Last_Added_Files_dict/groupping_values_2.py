lis=[{1: 2}, {2: 2}, {1: 3}, {2: 1}, {1: 3}]
new_lis=[{}]
for x in lis:
    for y in x:
       if y in new_lis[0]:
           new_lis[0][y].append(x[y])
           new_lis[0][y].sort()
       else :new_lis[0][y]=[x[y]]


print(new_lis)
# [{1: [2, 3, 3], 2: [1, 2]}]