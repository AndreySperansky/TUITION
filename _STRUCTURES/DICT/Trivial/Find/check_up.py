"""Проверить наличие в базе"""

people = {'Alice': {'phone': '234-0130', 'addr': 'Foo drive 23' },
          'Beth':  {'phone': '910-1265', 'addr': 'Bar street 42'}}
name = 'Alice'
key = 'phone'
if name in people:
  print( "%s phone is %s" % (name, people[name][key]))