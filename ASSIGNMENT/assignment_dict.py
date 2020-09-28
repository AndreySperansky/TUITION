input = [{1: 2}, {2: 2}, {1: 3}, {2: 1}, {1: 3}]

r = {}
for d in input:

# (assumes just one key/value per dict)
    (x, y), = d.items()
    r.setdefault(x, []).append(y)

print( [{k: v} for (k, v) in r.items()] )