def devision(arg1, arg2):
    try:
        res = arg1 / arg2
        print("{}/{} = {:.2f}".format(arg1, arg2, res))

    except ZeroDivisionError :
        print("Ошибка деления на ноль!")
    #return print("{}/{} = {:.2f}".format(arg1, arg2, res))


num1 = int(input('Введите числитель: '))
num2 = int(input('Введите знаменатель: '))

devision(num1, num2)