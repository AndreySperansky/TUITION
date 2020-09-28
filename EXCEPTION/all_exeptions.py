try:
	eval('print(7 / 4)a')
except ZeroDivisionError:
	print("Поймано исключение по нулю")
except SyntaxError:
	print('Поймано исключение Синтаксическая Ошибка')
except:
	print('Поймано какое-то исключение')

print("Программа завершена")



