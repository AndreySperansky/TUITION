L = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print(sum(L, []))
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

import itertools

L = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print(list(itertools.chain.from_iterable(L)))