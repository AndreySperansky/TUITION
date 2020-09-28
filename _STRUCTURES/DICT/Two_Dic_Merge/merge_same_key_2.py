dic1 = {'A': 25, 'B': 41, 'C': 32}
dic2 = {'A': 21, 'B': 12, 'C': 62}
result = {}
for key in (dic1.keys() | dic2.keys()):
    if key in dic1: result.setdefault(key, []).append(dic1[key])
    if key in dic2: result.setdefault(key, []).append(dic2[key])

print( result)

# {'C': [32, 62], 'A': [25, 21], 'B': [41, 12]}