from copy import deepcopy

x = {"user":'admin','attr':[1,2,3]}
y = x.copy()
print(y)
#{'user': 'admin', 'attr': [1, 2, 3]}

x['attr'].remove(1)
x['attr'].append("Mouse")
print(x)
print(y)

# {'user': 'admin', 'attr': [2, 3, 'Mouse']}
# {'user': 'admin', 'attr': [2, 3, 'Mouse']}

# Чтобы такого не получалось


y = deepcopy(x)
print(y)