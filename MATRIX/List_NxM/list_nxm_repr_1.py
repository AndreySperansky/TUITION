# matrix=[[]]
# matrix = [[0 for x in range(4)] for x in range(4)]

my_array1 = [[1, 2, 3],  [2, 3, 4],  [3, 4, 5]]

for elm in my_array1:
    ln = ""
    for i in elm:
        ln += str(i) + " "
    print(ln)

# 1 2 3
# 2 3 4
# 3 4 5