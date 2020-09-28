def mylist(val, lst=[]):
    lst.append(val)
    return lst

print( mylist(1))
print( mylist(2))



def mylist(val, lst=None):
    lst = lst or []
    lst.append(val)
    return lst

print( mylist(1))
print( mylist(2))