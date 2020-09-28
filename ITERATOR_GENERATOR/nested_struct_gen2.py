def chain(*iterables):
    for it in iterables:
        yield from it

g = chain([1, 2, 3], {'A', 'B', 'C'}, '...')
print(list(g))
# [1, 2, 3, 'A', 'B', 'C', '.', '.', '.']