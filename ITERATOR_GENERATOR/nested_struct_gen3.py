def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

g = chain([1, 2, 3], {'A', 'B', 'C'}, '...')
print(list(g))

# [1, 2, 3, 'A', 'B', 'C', '.', '.', '.']