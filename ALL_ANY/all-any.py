a= ['hello', 'hi', 'salut']
print(all(a))
print(any(a), '\n')

a= ['hello', '', 'salut']
print(all(a))
print(any(a), '\n')

a= ['', '', '']
print(all(a))
print(any(a), '\n')

# True
# True
#
# False
# True
#
# False
# False 