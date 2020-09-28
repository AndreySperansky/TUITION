d = {"user":'admin','attr':'1,2,3'}

key = 'attr'
value = 5

if key in d:

      d[key] = str(d[key]) + ',' + str(value)
else:
   d[key] = value

print(d)

# {'user': 'admin', 'attr': '1,2,3,5'}