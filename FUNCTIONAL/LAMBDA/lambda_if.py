f = lambda x: 'Like' if x > 100 else 'Subscribe'
print(f(10))
print(f(101) + '\n')
# Subscribe
# Like

d = lambda x: 'Like' if x > 100 else ('Subscribe' if x > 0 else 'follow me')

print(d(10))
print(d(101))
print(d(-1))

# Subscribe
# Like
# follow me



