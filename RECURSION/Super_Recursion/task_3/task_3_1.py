"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
try:
    NUM = abs(int(input("Введите число: ")))
    NUM_REV = 0
    while NUM > 0:
        digit = NUM % 10
        NUM = NUM // 10
        NUM_REV *= 10
        NUM_REV = NUM_REV + digit
    print("Реверсное число равно: ", NUM_REV)
except ValueError:
    print('Ошибка, нужно ввести целое число!')