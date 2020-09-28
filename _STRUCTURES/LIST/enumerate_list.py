array = ['10','11','12']

print(list(enumerate(array)))
# [(0, '10'), (1, '11'), (2, '12')]

for i, elem in enumerate(array):
    array[i] = int(elem)

print(array)
print(enumerate(array))
print(list(enumerate(array)))

# [10, 11, 12]
# <enumerate object at 0x0131A5F8>
# [(0, 10), (1, 11), (2, 12)]