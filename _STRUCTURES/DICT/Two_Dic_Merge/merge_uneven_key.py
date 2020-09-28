from collections import defaultdict

dicts = [{'a':1, 'b':2, 'c':3},
         {'a':1, 'd':2, 'c':'foo'},
         {'e':57, 'c':3} ]

# super_dict = defaultdict(set)  # uses set to avoid duplicates
#
# for d in dicts:
#     for k, v in d.items():  # use d.iteritems() in python 2
#         super_dict[k].add(v)
#
# # defaultdict(<class 'set'>, {'a': {1}, 'b': {2}, 'c': {3, 'foo'}, 'd': {2}, 'e': {57}})

super_dict = {}
for d in dicts:
    for k, v in d.items():
        if super_dict.get(k) is None:
            super_dict[k] = []
        if v not in super_dict.get(k):
            super_dict[k].append(v)


super_dict = {}
for k in set(k for d in dicts for k in d):
    super_dict[k] = set(d[k] for d in dicts if k in d)

# {'d': {2}, 'c': {3, 'foo'}, 'b': {2}, 'a': {1}, 'e': {57}}


super_dict = {}
for d in dicts:
    for k, v in d.items():
        super_dict.setdefault(k, []).append(v)
#
# # {'a': [1, 1], 'b': [2], 'c': [3, 'foo', 3], 'd': [2], 'e': [57]}

# import collections
# super_dict = collections.defaultdict(list)
# for d in dicts:
#     for k, v in d.items():
#         super_dict[k].append(v)
#
# # defaultdict(<class 'set'>, {'a': {1}, 'b': {2}, 'c': {3, 'foo'}, 'd': {2}, 'e': {57}})

# # Для избежания дублирования в списках используем	 set
# import collections
# super_dict = collections.defaultdict(set)
# for d in dicts:
#     for k, v in d.items():
#         super_dict[k].add(v)
#
# # defaultdict(<class 'set'>, {'a': {1}, 'b': {2}, 'c': {3, 'foo'}, 'd': {2}, 'e': {57}})

print(super_dict)