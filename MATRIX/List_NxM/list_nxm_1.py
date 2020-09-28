A = [[1, "a", 3, "d"], ['c', 'd', 'e', 'f'], [2, 3, 4, 5], [2, 3, 4, 5]]

# for i in range(len(A)):
#    for j in range(len(A[i])):
#        print(A[i][j], end = ' ')
#    print()


for row in A:
   for elem in row:
       print(elem, end = ' ')
   print()

# 1 a 3 d
# c d e f
# 2 3 4 5
# 2 3 4 5

# for row in A:
#    print(' '.join(map(str, row)))

# 1 a 3 d
# c d e f
# 2 3 4 5
# 2 3 4 5
