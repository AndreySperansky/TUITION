from collections import defaultdict

adic = [
		{"A": "VA1", "B": "VB1", "C": "VC1"},
		{"A": "VA2", "B": "VB2", "C": "VC2"},
        {"A": "VA3", "B": "VB3", "C": "VC3"},
		]

d = defaultdict(list)
for myd in adic:
    for k, v in myd.items():
        d[k].append(v)

print(d)
# defaultdict(<class 'list'>, {'A': ['VA1', 'VA2', 'VA3'], 'B': ['VB1', 'VB2', 'VB3'], 'C': ['VC1', 'VC2', 'VC3']})