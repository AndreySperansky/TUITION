x = {"user":'admin','attr':[1,2,3]}

print(x, '\n')
#{'user': 'admin', 'attr': [1, 2, 3]}

x['attr'].remove(1)
print(x, '\n')

# {'user': 'admin', 'attr': [2, 3]}

x['attr'].append("Mouse")
print(x)

# {'user': 'admin', 'attr': [2, 3, 'Mouse']}