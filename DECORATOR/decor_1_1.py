from datetime import datetime

def timeit(func):
	def wrapper(*args, **kwargs):
		start = datetime.now()
		result = func(*args, **kwargs)
		print(datetime.now() - start)
		return result
	return wrapper


@timeit
def one(n):
	# start = datetime.now()
	l = []
	for i in range(n):
		if i % 2 == 0:
			l.append(i)
	# print(datetime.now() - start)
	return l

@timeit
def two(n):
	# start = datetime.now()
	l = [x for x in range(n) if x % 2 == 0]
	# print(datetime.now() - start)
	return l

# l1 = one()
# l2 = two()

# print(l1)
# print(l2)

l1 = one         # Функция без скобок означает что она берется как объект
a = l1(10)
print(a)

l1 = timeit(one)        # => wrapper(10) эквивалентно @timeit
print(type(l1), l1.__name__)
a = l1(10000)

# Что эквивалетно следующей записи
l1 = timeit(one)(100000)    # => wrapper(10) эквивалентно @timeit
