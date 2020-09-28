"""3.Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов."""

def bestsum_two(num1, num2, num3):
    """
    Функция принимает три параметра, используется динамическая типизация
    :param nam1:    Число  (int, float)
    :param num2:    Число  (int, float)
    :param num3:    Число  (int, float)
    :return:   Сумма двух наибольших из трех
    """
    max_num = max(num1, num2, num3) + max(min(num1, num2), min(num1, num3), min(num2, num3))

    #Alternative

    # max_num = ''
    # if num1 > num2:
    #     if num2 > num3:
    #         max_num = num1 + num2
    #     else:
    #         max_num = num1 + num3
    # else:
    #     if num2 < num3:
    #         max_num = num2 + num3
    #

    return print(max_num)


a = 3
b = 5.5
c = 7.2

bestsum_two(a, b, c)