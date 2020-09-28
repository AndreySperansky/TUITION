a = ['ZZZ 800', 'aaa 45', 'eee  43', 'ddd 800',  'AaA 43', 'aaa 14',]

print(sorted(a, key = lambda x: (x.split()[0].lower(), int(x.split()[1]))))
# ['aaa 14', 'AaA 43', 'aaa 45', 'ddd 800', 'eee  43', 'ZZZ 800']

print(sorted(a, key = lambda x: int(x.split()[1])))
# ['aaa 14', 'eee  43', 'AaA 43', 'aaa 45', 'ZZZ 800', 'ddd 800']

a = sorted(a, key = lambda x: int(x.split()[1]))
a = sorted(a, key = lambda x: x.split()[0].lower(), reverse = True)
print(a)
# ['ZZZ 800', 'eee  43', 'ddd 800', 'aaa 14', 'AaA 43', 'aaa 45']

a = ['ZZZ 800', 'aaa 45', 'eee  43', 'ddd 800',  'AaA 43', 'aaa 14',]
a = sorted(a, key = lambda x: -int(x.split()[1]))
a = sorted(a, key = lambda x: x.split()[0].lower(), reverse = True)
print(a)
# ['ZZZ 800', 'eee  43', 'ddd 800', 'aaa 45', 'AaA 43', 'aaa 14']