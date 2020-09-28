def mylist(val, lst = []):	# mutable - переменчивый, непостоянный
	lst.append(val)
	return lst

print( mylist(1))
print( mylist(2))
print( mylist(4))
print( mylist(10))
print( mylist(100))

# [1]
# [1, 2]
# [1, 2, 4]
# [1, 2, 4, 10]
# [1, 2, 4, 10, 100]
