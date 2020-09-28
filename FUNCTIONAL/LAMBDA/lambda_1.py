

def knights():
    title = 'Sir'
    action = (lambda x: title + ' '  + x) # Заголовок в объемлющей def
    return action # Возвращает функцию


# Вызов переменной с параметрами
act = knights()
print(act('robin'))
#'Sir robin’

f = lambda x, y, z: x + y + z
print(f(2, 3, 4))


# найти сумму двух больших из трех
my_func2 = lambda a,b,c: max(a+b, b+c, a+c)
print(my_func2(3,5,7))

devidion2 = lambda a, b: a / b if b else None