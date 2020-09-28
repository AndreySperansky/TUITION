from collections import defaultdict
#
# dic1 = {'A': 25, 'B': 41, 'C': 32}
# dic2 = {'A': 21, 'B': 12, 'C': 62}
#
#
# # the preperation
#
# dicts = [dic1, dic2]
# final = defaultdict(list)
#
# # the logic
# for k, v in ((k, v) for d in dicts for k, v in d.items()):
#     final[k].append(v)
#
# print(final)
#
# # defaultdict(<class 'list'>, {'A': [25, 21], 'B': [41, 12], 'C': [32, 62]})