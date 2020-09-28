
def miles_to_kilometers(num_miles):
	""" Converts miles to the kilometers """
	return num_miles * 1.6

"""MAP  сфункцией созданной пользователями"""

mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(miles_to_kilometers, mile_distances))
print(kilometer_distances)

# [1.6, 10.4, 27.84, 3.84, 14.4]


# То же самое только с lambda аункцией

mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))

print(kilometer_distances)

# [1.6, 10.4, 27.84, 3.84, 14.4]