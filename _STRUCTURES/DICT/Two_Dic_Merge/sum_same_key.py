from functools import reduce

data = {
    "2010":{
            'A':2,
            'B':3,
            'C':5,
            'D':-18,
        },
    "2011":{
            'A':1,
            'B':2,
            'C':3,
            'D':1,
        },
    "2012":{
            'A':1,
            'B':2,
            'C':4,
            'D':2
        }
    }

print(reduce(lambda x, y: dict((k, v + y[k]) for k, v in x.items()), data.values()))

# {'A': 4, 'B': 7, 'C': 12, 'D': -15}

