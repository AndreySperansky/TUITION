arg1 = 100
arg2 = 0

try:
	res = arg1 / arg2
except ZeroDivisionError:
	print("Нельзя делить на 0!!!")
else:
	print("{}/{} = {:.2f}".format(arg1, arg2, res))
finally:
	print("Программа завершена!")