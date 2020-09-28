import itertools

"""dropwhile() ничего не выдает, пока выполняется условие, зато потом выдает все без остатка."""

for i in itertools.dropwhile(lambda x: x > 0, [1, -2, 3, -3]):
	print(i)