"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def recur_odd_even(num, even=0, odd=0):
    # Все цифры числа извлечены
    if num == 0:
        return even, odd
    
    else:
        # достаем очередную цифру числа
        cur_n = num % 10
        # число, естественно, становится короче
        num = num // 10
        # проверяем цифра четная или нечетная
        if cur_n % 2 == 0:
            even += 1
            return recur_odd_even(num, even, odd)
        else:
            odd += 1
            return recur_odd_even(num, even, odd)


try:
    num = (int(input("Введите натуральное число: ")))
    print(f'Количество четных и нечетных цифр в числе равно {recur_odd_even(num)}')
except ValueError:
    print('Ошибка, нужно ввести целое число!')