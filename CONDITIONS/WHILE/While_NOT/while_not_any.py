lst = ['c1', 'c2', 'NOT', 'c3']

while not any(word in lst for word in ['AND', 'OR', 'NOT']):
    print( 'No boolean')


MyOper = set(['AND', 'OR', 'NOT'])
MyList = set(['c1', 'c2', 'NOT', 'c3'])

while not MyList.isdisjoint(MyOper):
    print( "No boolean Operator")

while ('AND' not in lst and
       'OR' not in lst and
       'NOT' not in lst):
    print( 'No Boolean Operator')

s = set(["AND", "OR", "NOT"])
while not s.intersection(s):
	print('No Boolean Operator')



while not any(x in ('AND', 'OR', 'NOT') for x in list):
	print('No Boolean Operator')

while not ('AND' in list, 'OR' in list, 'NOT' in list) == (False, False, False):
	print('No Boolean Operator')



while 'AND' not in MyList and 'OR' not in MyList and 'NOT' not in MyList:
	print( 'No Boolean Operator')