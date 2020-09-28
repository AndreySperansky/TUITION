in_file = "our_input.txt"
out_file = "output.txt"
f = open(in_file)
g = open(out_file, "w")
for line in f:
	if line == "\n":
		g.write("0\n")
	else:
		g.write(str(line.count(" ") + 1) + "\n")