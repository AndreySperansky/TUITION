a, *b = 'spam' 						# Расширенная операция распаковывания последовательностей (Python 3.0)

a, *b = 'spam'
print(a)
#   's'
print(b)
#   ['p', 'a', 'm']

spam = ham = 'lunch' 		# Групповое присваивание одного значения
print(ham)

spam += '42' 				# Комбинированная инструкция присваивания (эквивалентно инструкции spam = spam + '42')
print(spam)