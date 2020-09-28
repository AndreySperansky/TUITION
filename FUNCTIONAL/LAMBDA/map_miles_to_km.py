mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))

print(kilometer_distances)

# [1.6, 10.4, 27.84, 3.84, 14.4]