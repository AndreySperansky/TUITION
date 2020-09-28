"""!"""
"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""
class OwnZeroDivError(Exception):
	def __init__(self, message: str):
		self.message = message
		#Exception.__init__(self)


class MyDivError:
	def __init__(self, arg1, arg2):
		self.num1 = arg1
		self.num2 = arg2
		while type(self.num1) != int or type(self.num2) != int:  # Запускаем цикл проверки типа значеня
			self.num1 = input('Введите числитель: \n')
			self.num2 = input('Введите знаменатель: \n')
			try:
				self.num1 = int(self.num1)
				self.num2 = int(self.num2)
			except ValueError:
				print('Ошибка, нужно вводить целое число! \n')


	def fdivision(self):
		try:
			if self.num2 == 0:
				raise OwnZeroDivError("Ошибка! Делить на ноль нельзя!")

		except OwnZeroDivError as err:
			print(err)

		else:
			res = self.num1 / self.num2
			return print("{}/{} = {:.2f}".format(self.num1, self.num2, res))

clsp = MyDivError(50, "2")
res = clsp.fdivision()