def readfilesimple(my_file):
	linecounter = 0
	with open(my_file,'r') as foo:
		for lines in foo:
			linecounter += 1

	return linecounter

# count=0
# with open ('filename.txt','rb') as foo:
#     for lines in f:
#         count += 1
#
# print(count)
