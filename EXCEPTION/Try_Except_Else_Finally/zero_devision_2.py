""" 1.Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def devision(arg1, arg2):
    try:
        res = arg1 / arg2
        #print("{}/{} = {:.2f}".format(arg1, arg2, res))

    except ZeroDivisionError :
        print("Ошибка! Делить на ноль нельзя!")
    else:
        return print("{}/{} = {:.2f}".format(arg1, arg2, res))

num1 = num2 = ''                                # объявляем числитель и знаменатель
while type(num1) != int or type(num2) != int:   # Запускаем цикл проверки типа значеня
    num1 = input('Введите числитель: \n')
    num2 = input('Введите знаменатель: \n')
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print('Введите целое число! \n')



devision(num1, num2)