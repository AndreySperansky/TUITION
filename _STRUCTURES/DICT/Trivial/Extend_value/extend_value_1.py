d = {"user":'admin','attr':[1,2,3]}

key = 'attr'
value = 5

if key in d:
   try:
      d[key].append(value)
   except AttributeError:
      d[key] = [d[key], value]
else:
   d[key] = value

print(d)

# {'user': 'admin', 'attr': [1, 2, 3, 5]}