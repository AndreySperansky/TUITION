"""Суммы строк и столбцов матрицы"""

from random import randint
N = 5
M = 10

EXT_LST = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(0, 10))
        print(f"{b[j]:4d}", end='')
    EXT_LST.append(b)
    print('   |', sum(b))

for i in range(M):
    print(f" ---", end='')
print()

for i in range(M):
    s = 0
    for j in range(N):
        s += EXT_LST[j][i]
    print(f"{s:4d}", end='')
print()


# 4  10   9   8   8   4   2   1   7   7   | 60
# 7   0   7   9   4   6   9   3   3   9   | 57
# 0   2   0   1   5   1   5   4   5   5   | 28
# 2   9   3   1   6   7   8   1   7   2   | 46
# 8   4   8   4   8   8   7   1   0   4   | 52
# --- --- --- --- --- --- --- --- --- ---
# 21  25  27  23  31  26  31  10  22  27