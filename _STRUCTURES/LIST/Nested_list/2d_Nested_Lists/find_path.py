def findPath(t, x):
    if t[0] == x:
        return [t[0]]
    for path in [findPath(branch, x) for branch in t[1:]]:
        if path:
            return [t[0]] + path


t = [1, [3, [4], [5]], [2]]

print(findPath(t, 5))
# returns [1,3,5]
print(findPath(t, 2))
# returns [1 ,2]
print(findPath(t, 4))