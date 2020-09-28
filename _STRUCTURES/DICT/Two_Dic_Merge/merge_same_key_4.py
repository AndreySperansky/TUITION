data = [ {"A": "value1", "B": "value2", "C": "value3"},
         {"A": "value4", "B": "value5", "C": "value3"},
         {"A": "value1", "B": "value8", "C": "value3"} ]

keylist = data[0].keys()
mydata = dict((k, ', ' .join(set(map(lambda d: d[k], data)))) for k in keylist)
print(mydata)

# {'A': 'value4, value1', 'B': 'value5, value2, value8', 'C': 'value3'}