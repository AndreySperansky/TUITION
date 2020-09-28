import collections

data = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

data.move_to_end('d', last=False)

print(data)