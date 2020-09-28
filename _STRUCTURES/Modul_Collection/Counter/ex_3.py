from collections import Counter

a = Counter('superfluous')

# Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})
print(a)

counter = Counter('superfluous')
print(counter['u'])  # 3


print(list(counter.elements()))
# ['e', 'l', 'f', 'o', 'r', 's', 's', 'p', 'u', 'u', 'u']


print(counter.most_common(2))
# [('u', 3), ('s', 2)]