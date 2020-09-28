"""hw_5_3"""
"""программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

fname = input('Введите имя файла "filename.txt": \n')
foo = open(fname, 'w', encoding="utf-8")
str = input("Введите строку из любых чисел через пробел:  \n")
foo.write(str+'\n')
foo.close()

foo = open(fname, 'r', encoding="utf-8")
num_list = foo.read().split()
foo.close()
sum_num = 0
for elm in num_list:
	sum_num += int(elm)

print(f"Сумма введенных чисел равна: {sum_num}")
