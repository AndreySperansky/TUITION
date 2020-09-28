def f(a, l = []):
  l.append(a)
  return l
print( f(1))
print( f(2))
print( f(3))

# [1]
# [1, 2]
# [1, 2, 3]



def foo2(x=None):
    if x is None:
        x=[]
    x.append(1)
    print(x)

foo2() # [1]
foo2() # [1]
foo2() # [1]