heroes = {
		'Spider-Man': 80,
		'Batman': 65,
		'Superman': 85,
		'Wonder Woman': 70,
		'Flash': 70,
		'Iron Man': 65,
		'Thor': 90,
		'Aquaman': 65,
		'Captain America': 65,
		'Hulk': 87,
}
for i in sorted(heroes.values()):
	print(i, end = " ")
# 65 65 65 65 70 70 80 85 87 90

for i in sorted(heroes.items(), key = lambda para: para[1]):
	print(i)

# ('Iron Man', 65)
# ('Aquaman', 65)
# ('Captain America', 65)
# ('Wonder Woman', 70)
# ('Flash', 70)
# ('Spider-Man', 80)
# ('Superman', 85)
# ('Hulk', 87)
# ('Thor', 90)