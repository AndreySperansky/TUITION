
d = {"user":'admin', 'attr':[1,2,3]}

def extend_dictionary(d, key, value):
   if key in d:
      if isinstance(d[key], list):
         d[key].append(value)
      else:
         d[key] = [d[key], value]
   else:
      d[key] = value

ext = extend_dictionary(d, 'attr', 4)

print(d)

# {'user': 'admin', 'attr': [1, 2, 3, 4]}



