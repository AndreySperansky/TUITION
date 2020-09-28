import itertools

# Original dict
a = {"A": ("1st/dir", "hello.txt"),
     "B": ("2nd/dir", "foo.txt"),
     "C": ("1st/dir", "hello.txt"),
     "D": ("1st/dir", "hello.txt"),
     "F": ("3rd/dir", "dog.txt")}

# Convert dict to sorted list of items
a = sorted(a.items(), key=lambda x:x[1])
# print(a)

# Group by value of tuple
groups = itertools.groupby(a, key=lambda x:x[1])
#print(groups)

# Pull out matching groups of items, and combine items
# with no matches back into a single dictionary
remainder = []
matched   = []

for key, group in groups:
   group = list(group)
   if len(group) == 1:
      remainder.append(group[0])
   else:
      matched.append(dict(group))
else:
   remainder = dict(remainder)

print(matched)
print(remainder)

# [{'A': ('1st/dir', 'hello.txt'), 'C': ('1st/dir', 'hello.txt'), 'D': ('1st/dir', 'hello.txt')}]
# {'B': ('2nd/dir', 'foo.txt'), 'F': ('3rd/dir', 'dog.txt')}