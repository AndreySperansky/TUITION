alst = [1, 2, 3, 4, 5]
blst = [6, 7, 8, 9, 10]

for i in range(5):
    blst[i]=alst[i]
print(blst)
# [1, 2, 3, 4, 5]

for k in range(5):
    blst[k]=blst[k]*2
print(blst)
# [2, 4, 6, 8, 10]
print(alst)
# [1, 2, 3, 4, 5]

clst=alst
clst[1] = 50
print(clst)
# [1, 50, 3, 4, 5]
print(alst)
# [1, 50, 3, 4, 5]





