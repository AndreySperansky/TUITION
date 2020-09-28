# Удалит существующую информацию в some.txt и запишет "Hello".
my_file = open("some.txt", 'w')
my_file.write("Hello")
my_file.close()

# Оставит существующую информацию в some.txt и добавит "Hello".
my_file = open("some.txt", 'a')
my_file.write("Hello, world!")
my_file.close()