from datetime import datetime

def timeit(arg):
	print(arg)
	def outer(func):
		def wrapper(*args, **kwargs):
			start = datetime.now()
			result = func(*args, **kwargs)
			print(datetime.now() - start)
			return result
		return wrapper
	return outer


@timeit('name')
def one(n):
	# start = datetime.now()
	l = []
	for i in range(n):
		if i % 2 == 0:
			l.append(i)
	# print(datetime.now() - start)
	return l

@timeit('name')
def two(n):
	# start = datetime.now()
	l = [x for x in range(n) if x % 2 == 0]
	# print(datetime.now() - start)
	return l

# name
# name


two(10000)
# 0:00:00.002001

l1 = timeit('name')(one)(100000)
# name
# 0:00:00.027019
# 0:00:00.028021
