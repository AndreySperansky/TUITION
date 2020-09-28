import itertools

"""takewhile() дает значения, пока условие истинно, а остальные значения
даже не берет из итератора (именно не берет, а не высасывает все до конца!)"""

for i in itertools.takewhile(lambda x: x > 0, [1, -2, 3, -3]):
	print(i)