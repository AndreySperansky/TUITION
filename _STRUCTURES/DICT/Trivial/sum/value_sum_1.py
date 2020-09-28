


from collections import defaultdict

d = {'dom': '319', 'So': '546', 'so': '15', 'Dom': '6'}

d1 = defaultdict(int)

for key, value in d.items():
    d1[key.lower()] += int(value)

print(d1)
# defaultdict(<class 'int'>, {'dom': 325, 'so': 561})

dd = dict()
for i in d:
    key = i.lower()
    if key in dd:
        dd[key] += int(d[i])
    else:
        dd[key] = int(d[i])

print(dd)
# {'dom': 325, 'so': 561}


for k, v in d.items():
    k = k.lower()
    dd[k] = dd.get(k, 0) + int(v)

print(dd)

# {'dom': 650, 'so': 1122}