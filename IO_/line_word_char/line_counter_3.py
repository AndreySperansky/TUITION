
def main():

	file = open("infile.txt",'r')
	count = 0
	for line in file:
		count+=1

	print (count)

main ()