# ������ ������������ ���������� � some.txt � ������� "Hello".
my_file = open("some.txt", 'w')
my_file.write("Hello")
my_file.close()

# ������� ������������ ���������� � some.txt � ������� "Hello".
my_file = open("some.txt", 'a')
my_file.write("Hello, world!")
my_file.close()