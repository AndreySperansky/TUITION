
S = 'spam'
print(S)
print('Последний элемент в конце S')
print(S[-1] + " \n ")
print('Второй элемент с конца')
print(S[-2] + " \n ")
print('Отрицательная индексация, более сложный способ')
print(S[len(S) - 1] + " \n ")
print('Срез строки S начиная со смещения 1 и до 2 (не 3)')
print(S[1:3] + ' \n ')
print('Все, кроме первого элемента (1:len(S))')
print(S[1:] + ' \n ')
print('Все, кроме последнего элемента')
print(S[0:3] + ' \n ')
print('То же, что и S[0:3]')
print(S[:3] + ' \n ')
print('Еще раз все, кроме последнего элемента, но проще (0:-1)')
print(S[:-1] + ' \n ')
print('Все содержимое S, как обычная копия (0:len(S))')
print(S[:] + ' \n ')
print('Конкатенация')
print(S + 'XYZ' + '  \n ')
print('Повторение \n')
print(S * 8 + ' \n')

print('S[0] = "z"  # Неизменяемые объекты нельзя изменить Python выдаст ошибку \n')
print('Но с помощью выражений мы можем создавать новые объекты')
S = 'z' + S[1:]

print(S)
print('Поиск смещения подстроки')
S.find('pa')
print('\n')
print(S.find('pa'))
print('Замена одной подстроки другой')
S.replace('pa', 'XYZ')
print('\n')
print(S.replace('pa', 'XYZ'))

S = 'spam'
print('Преобразование символов в верхний и в нижний регистр')
print(S.upper())
print('\n')
line = 'aaa,bbb,ccccc,dd'

print('Разбивает строку по разделителю и создает список строк')

line = line.split(',')
print(line, '\n')

line = 'aaa,bbb,ccccc,dd'


print ('Удаляет завершающие пробельные символы', '\n')
line = line.rstrip()
print(line, '\n')


print('%s, eggs, and %s' % ('spam', 'SPAM!', '\n'))  # Выражение (во всех версиях)

print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))  # Метод (2.6, 3.0)