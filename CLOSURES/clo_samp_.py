'''!'''
"""Замыкание это функция в теле которой есть сылки на перменные которые были объявлены вне ее тела  и не
являются параметрами этой функции
окружающая область видимости таких переменых назвается inclosing"""

def foo(x):
	x = 1
	
# print(x)
# NameError: name 'x' is not defined
# Здесь объект foo(x) перестал существовать и x  почищен garbage collector


def one():
	x = ['one', 'two']
	def inner():
		print(x)
		print(id(x))    # id объекта на который указывает ссылка переменной х
	return inner        # в этом примере функция вызывется как объект (без скобок)
	
o = one()
print(o)
# <function one.<locals>.inner at 0x0150E7C8>

print(o())
# ['one', 'two']
# 5522936

print(dir(o))
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__',
#  '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__',

print(o.__closure__)
# (<cell at 0x00A4F370: list object at 0x009E45F8>,)

print(dir(o.__closure__[0]))
# __setattr__', '__sizeof__', '__str__', '__subclasshook__', 'cell_contents']

print(o.__closure__[0].cell_contents)
# ['one', 'two']

a = o.__closure__[0].cell_contents
print(id(a))
# 5522936


a.append('any')
print(o())
# ['one', 'two', 'any']
# 5522936

