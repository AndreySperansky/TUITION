"""get() — получает значение по ключу, в случае отсутствия дает None:"""

d = {'name1':'two'}
print(d.get('name'))
print(d.get('name1'))
# None
# two