exampleSet = [{'type':'type1'},
              {'type':'type2'},
              {'type':'type2'},
              {'type':'type3'}
              ]

keyValList = ['type2','type3']
expectedResult = [d for d in exampleSet if d['type'] in keyValList]
print(expectedResult)

# 2 вариант

res = list(filter(lambda d: d['type'] in keyValList, exampleSet))
print(res)
# [{'type': 'type2'}, {'type': 'type2'}, {'type': 'type3'}]

# 3 вариант

from itertools import filterfalse
for elem in filterfalse(lambda x: x['type'] not in keyValList, exampleSet):
    print( elem)


