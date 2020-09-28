keys=['spam', 'eggs', 'toast']
vals=[1,3,5]
print(list(zip(keys, vals)))

# [('spam', 1), ('eggs', 3), ('toast', 5)]

D2 = {}
for (k, v) in zip(keys, vals):
    D2[k] = v
print(D2)

# {'spam': 1, 'eggs': 3, 'toast': 5}