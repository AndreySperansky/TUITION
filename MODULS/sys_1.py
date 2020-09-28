import sys, os

"""
Пример консольного приложения, когда все параметры получаются из командной строки в терминале
"""

print(sys.path)


print(sys.argv[0])

def ping():
	print('pong')


def hello(name):
	print('hello', name)

def get_info():
	print(os.listdir())

command = sys.argv[1]

if command == 'ping':
	ping()

elif command == 'list':
	get_info()

elif command == 'name':
	name = sys.argv[2]
	hello(name)

"""
Для перехода в дерикторию использовать консольг=ную команду cd C:\Users\Andrey_User\PycharmProjects\TUTION\MODULS 

или просто зацепить файл и перетащить его в консоль
"""