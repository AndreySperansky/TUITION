s = "*" * 60
n = 5
print(s)
# import textwrap
# print( textwrap.wrap(s, n))
# ['*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*']

# parts = [s[i:i+ n] for i in range(0, len(s), n)]
# print(parts)
# ['*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*']

# print(list(map(''.join, zip(*[iter(s)]*n))))
# ['*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*****', '*']

#print(s.split('#', n))
chunks = [s[x:x+n] for x in range (0, len(s), n)]
#chunks = [s[i - n:i] for i in range(n, len(s) + 1, n)]
new = r"\n".join(chunks)

#chunks = map(''.join, zip(*[iter(s)] * n))
print(chunks)
print(new)

	# в виде обычной функции
# def chunks(lst, chunk_size):
# 	return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]
#
# chunks(list(range(10)), 2)
# [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]

	# или в виде генератора
# def chunks(lst, chunk_size):
# 	for i in range(0, len(lst), chunk_size):
# 		yield lst[i : i+chunk_size]
#
# for i in chunks(list(range(10)), 2):
# 	print(i)


# [0, 1]
# [2, 3]
# [4, 5]
# [6, 7]
# [8, 9]


# s = 'reserved-memory,NO,NO,NO,,NO,"^({1,20})$",,,,,,,cache-policy=^(RESIDENT|NO_MIGRATION)$,,,'
# def comma_split(s):
#     if s.count(',') > 1:
#         return s.split(',')
#     return s
# def reduce_flat(a, b):
#     if isinstance(b, list):
#         a = a +  b
#     else:
#         a.append(b)
#     return a
# print reduce(reduce_flat, map(comma_split, s.split('"')), [])

a = r"***********"
b = r"******"

print(a+b)
print((len(a)-len(b)) * '*')