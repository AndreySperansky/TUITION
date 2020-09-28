a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)


#1 2
#2 1

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)
    
# 1 2 3
# 4 5 6