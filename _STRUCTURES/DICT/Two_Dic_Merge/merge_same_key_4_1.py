from itertools import chain
from collections import defaultdict

data = [ {"A": "value1", "B": "value2", "C": "value3"},
         {"A": "value4", "B": "value5", "C": "value3"},
         {"A": "value1", "B": "value8", "C": "value3"} ]

res = dict([ (key, ",".join(set([elem[key] for elem in data]))) for key in set(list(chain(*[d.keys() for d in data])))])

print(res)
# {'A': 'value4,value1', 'C': 'value3', 'B': 'value8,value2,value5'}


