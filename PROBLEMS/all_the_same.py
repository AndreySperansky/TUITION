def all_the_same(elements):
	return len(set(elements)) == 1





# These "asserts" are used for self-checking and not for an auto-testing
assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same(['a', 'a', 'a']) == True
# assert all_the_same([]) == True
assert all_the_same([1]) == True
print("Coding complete? Click 'Check' to earn cool rewards!")


