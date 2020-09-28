all_pairs = []
for i in range(5):
	for j in range(5):
		# if i <= j:
		# 	all_pairs.append((i, j))
		all_pairs.append((i, j))
print(all_pairs, '\n')


"""Все это можно записать в виде спискового включения так:"""

all_pairs2 = [(i, j) for i in range(5) for j in range(5) if i <= j]
print(all_pairs2)