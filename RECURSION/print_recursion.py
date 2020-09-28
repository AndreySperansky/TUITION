L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

""" 1 [2, 3, 4]
    2 [3, 4]
    3 [4]
    4 []        """