"""15. Нахождение наиболее часто повторяющихся элементов списка"""

a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(max(set(a), key=a.count))
# 2

from collections import Counter

a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
cnt = Counter(a)
print(cnt.most_common(3))
# [(2, 4), (1, 3), (3, 2)]