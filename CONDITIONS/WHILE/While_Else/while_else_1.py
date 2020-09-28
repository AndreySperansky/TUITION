do = True
while do:
	print('делаем')
	do = False
	print('делаем')
else:
	print('закончили \n')

# делаем
# делаем
# закончили

"""     break
Если в теле цикла встречается инструкция break, то цикл завершается, при этом блок else не выполняется."""

do = True
while do:
	print('делаем \n')
	break
	do = False
	print('делаем')

else:
	print('закончили \n')

# делаем

"""continue
Если в теле цикла встречается инструкция continue, то остаток тела цикла пропускается и производится переход к очередной
проверке истинности."""

do = True
while do:
	print('делаем')
	do = False
	continue
	print('делаем')

else:
	print('закончили')

# делаем
# закончили