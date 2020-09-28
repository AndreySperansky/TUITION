# Сортирвка с помощью анонимных функций

a = ['ZZZ 79', 'aaa 45', 'eee  43', 'DDD 800',  'BBB 5', 'www 14',]

print(sorted(a, key = lambda x: int(x.split()[1]) ))
# ['BBB 5', 'www 14', 'eee  43', 'aaa 45', 'ZZZ 79', 'DDD 800']

a = ['ZZZ 800', 'aaa 45', 'eee  43', 'ddd 800',  'BBB 43', 'www 14',]
print(sorted(a, key = lambda x: int(x.split()[1]) ))
# ['www 14', 'eee  43', 'BBB 43', 'aaa 45', 'ZZZ 800', 'ddd 800']

print(sorted(a, key = lambda x: (int(x.split()[1]),  x.split()[0]) ))
# ['www 14', 'BBB 43', 'eee  43', 'aaa 45', 'ZZZ 800', 'ddd 800']

print(sorted(a, key = lambda x: (int(x.split()[1]),  x.split()[0].lower()) ))
# ['www 14', 'BBB 43', 'eee  43', 'aaa 45', 'ddd 800', 'ZZZ 800']

print(sorted(a, key = lambda x: (x.split()[0].lower(), int(x.split()[1])) ))
# ['aaa 45', 'BBB 43', 'ddd 800', 'eee  43', 'www 14', 'ZZZ 800']

print(sorted(a, key = lambda x: (int(x.split()[1]),  x.split()[0].lower()), reverse = True ))
# ['ZZZ 800', 'ddd 800', 'aaa 45', 'eee  43', 'BBB 43', 'www 14']

