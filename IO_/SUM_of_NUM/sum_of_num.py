"""hw_5_3"""
"""����������) ��������� ����, �������� � ���� ���������� ����� �����, ����������� ���������. 
��������� ������ ������������ ����� ����� � ����� � �������� �� �� �����."""

fname = input('������� ��� ����� "filename.txt": \n')
foo = open(fname, 'w', encoding="utf-8")
str = input("������� ������ �� ����� ����� ����� ������:  \n")
foo.write(str+'\n')
foo.close()

foo = open(fname, 'r', encoding="utf-8")
num_list = foo.read().split()
foo.close()
sum_num = 0
for elm in num_list:
	sum_num += int(elm)

print(f"����� ��������� ����� �����: {sum_num}")
