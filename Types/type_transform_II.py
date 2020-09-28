print ('\n')
print(0.1 + 0.1 + 0.1 - 0.3)

from decimal import Decimal
print (Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

print ('\n')

import decimal
print (decimal.Decimal(1) / decimal.Decimal(7))
# 0.1428571428571428571428571429

print ('\n')

decimal.getcontext( ).prec = 4
print (decimal.Decimal(1) / decimal.Decimal(7))
# 0.1429

print ('\n')

print (1999 + 1.33)
decimal.getcontext().prec = 2
pay = decimal.Decimal(str(1999 + 1.33))
print (pay)
# 2000.33

print ('\n  ДРОБИ =========================================================')
"""как и Decimal, класс Fraction находится в модуле. Чтобы создать
объект этого типа, необходимо импортировать модуль и вызвать конструктор
класса, передав ему числитель и знаменатель"""

from fractions import Fraction
x = Fraction(1, 3) 			# Числитель, знаменатель
y = Fraction(4, 6) 			# Будет упрощено до 2, 3 с помощью функции gcd

print(x)
# 1/3
print(y)
# 2/3


print ('\n')

print (x + y)
print (repr(x + y))
# Fraction(1, 1)

# print (x – y) 		# НЕ РАБОТАЕТ !!!!!!		# Точный результат: числитель, знаменатель
# Fraction(-1, 3)

print (repr(x * y))
# Fraction(2, 9)



print ('\n =================================================================================')

print (Fraction(6, 12)) 			# Будет упрощено автоматически
# Fraction(1, 2)

print (Fraction(1, 3) + Fraction(6, 12))
# Fraction(5, 6)

print (decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12)))
# Decimal('0.83')

print ('\n=============================================================================')

print (1000.0 / 1234567890)
# 8.1000000737100011e-07

print (Fraction(1000, 1234567890))
# Fraction(100, 123456789)

print ((2.5).as_integer_ratio())   # метод объекта типа float
# (5, 2)

"""символ * во втором примере – это специальный
синтаксис распаковывания кортежа в отдельные аргументы – подробнее об
этом будет рассказываться в главе 18(ЛУЦ)"""

f = 2.5
z = Fraction(*f.as_integer_ratio()) 	# Пеобразование float -> fraction:
print (z) 						# два аргумента
# Fraction(5, 2) 			# То же самое, что и Fraction(5, 2)

print ('\n=============================================================================')

print (x) 						# x – из предыдущего примера сеанса
# Fraction(1, 3)

print (x + z)
#Fraction(17, 6)             # 5/2 + 1/3  =  15/6 + 2/6