line = "hello3 bu 34 5kdf45"

#line = input()
num_out_of_line = []
str_num = ""

for i in range(len(line)):
	if line[i] in "0123456789":
		str_num += line[i]
		try:
			if line[i + 1] not in "0123456789":
				num_out_of_line.append(str_num)
				str_num = ""
		except:
			num_out_of_line.append(str_num)

print(list(map(int, num_out_of_line)))