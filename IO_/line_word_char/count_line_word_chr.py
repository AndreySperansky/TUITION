#import sys
#fname = sys.argv[1]		# для случия получения файла через командную строку

with open('my_file1.txt', "r", encoding="UTF-8") as foo:
# foo = open('my_file1.txt', "rw")

	lines = 0
	words = 0
	letters = 0

	for line in foo:
	#for line in open(foo):
		lines += 1
		letters += len(line)

		pos = 'out'
		for letter in line:
			if letter != ' ' and pos == 'out':
				words += 1
				pos = 'in'
			elif letter == ' ':
				pos = 'out'

print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)

#foo.close()