print('That is %d %s bird!' % (1, 'dead')) # Выражение форматирования
#That is 1 dead bird!

print("%d %s %d you" % (1, 'spam', 4))
#'1 spam 4 you'

print('\n')

print ("Units destroyed: {players[0]} ".format(players = [1, 2, 3]))
#'Units destroyed: 1'

print ("Units destroyed: {players[0]!r:*<20s} ".format(players = ['1', '2', '3']))
#Units destroyed: '1'*****************


print ("Units destroyed: {players[0]:*<20s!r} ".format(players = ['1', '2', '3']))
#Units destroyed: '1'*****************

print('\n ==============================================================================')


print ("%(n)d %(x)s" % {"n":1, "x":"spam"})
'1 spam'

reply = """ 					# Шаблон с замещаемыми спецификаторами формата
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""
values = {'name': 'Bob', 'age': 40} # Подготовка фактических значений
print (reply % values) # Подстановка значений

#Greetings...
#Hello Bob!
#Your age squared is 40


""""способ также часто используется в комбинации со встроенной функцией
vars, которая возвращает словарь, содержащий все переменные, существую-
щие на момент ее вызова:"""


food = 'spam'
age = 40
vars()
#{'food': 'spam', 'age': 40, ...и еще множество других... }

"""Если задействовать эту функцию в правой части оператора форматирования,
можно отформатировать значения, обращаясь к ним по именам переменных
(то есть по ключам словаря):"""

print("%(age)d %(food)s" % vars())
#'40 spam'

#==========================================================================================
print('\n')


template = '{0}, {1} and {2}' # Порядковые номера позиционных аргументов
print (template.format('spam', 'ham', 'eggs'))
#'spam, ham and eggs'

template = '{motto}, {pork} and {food}' 				# Имена именованных аргументов
print (template.format(motto='spam', pork='ham', food='eggs'))
#'spam, ham and eggs'

template = '{motto}, {0} and {food}' 					# Оба варианта
print(template.format('ham', motto='spam', food='eggs'))
#'spam, ham and eggs'

#===========================================================================================
print('\n')


import sys
print('My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'}))
#'My laptop runs win32'
print('My {config[spam]} runs {sys.platform}'.format(sys=sys, config={'spam': 'laptop'}))
#'My laptop runs win32'

"""как вы узнаете в главе 18, аргумент **data в вызове метода – это специальный
синтаксис распаковывания ключей и значений словарей в отдельные пары
«name=value» именованных аргументов, благодаря чему появляется возмож-
ность обращаться к ним по именам в строке формата):"""

# В обоих случаях используются данные, собранные предварительно

data = dict(platform=sys.platform, spam='laptop')
print('My {spam:<8} runs {platform:>8}'.format(**data))
#'My laptop runs win32'

print('My %(spam)-8s runs %(platform)8s' % data)
#'My laptop runs win32'