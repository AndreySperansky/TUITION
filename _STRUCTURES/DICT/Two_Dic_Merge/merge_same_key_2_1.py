import collections

dic1 = {'A': 25, 'B': 41, 'C': 32}
dic2 = {'A': 21, 'B': 12, 'C': 62}

def combineDict(dict1, dict2):
    res = collections.defaultdict(list)
    for key, value in (dict1.items() | dict2.items()):
        res[key].append(value)
    return res

print(combineDict(dic1, dic2))

# defaultdict(<class 'list'>, {'C': [32, 62], 'B': [41, 12], 'A': [21, 25]})