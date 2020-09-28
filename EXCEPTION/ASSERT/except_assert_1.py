# Исключения и утверждения могут проверять параметры функции,
# выступая в т.ч. более строгим вариантом документации


def fact(x):
    """Вернуть факториал 'x'.

    Не передавайте числа больше 15 во избежание переполнения памяти.
    """
    if x <= 1:
        return 1
    else:
        return x * fact(x-1)


def fact_save_1(x):
    assert x <= 15, \
        "Не передавайте числа больше 15 во избежание переполнения памяти"

    return fact(x)


def fact_save_2(x):
    if not x <= 15:
        raise ValueError("Не передавайте числа больше 15 во избежание "
                         "переполнения памяти")

    return fact(x)


print("{:>3} {:>20} {:>20}".format(*("x", "fact()", "fact_save()")))
for x in (5, 20):
    print("{:3}".format(x), end=" ")
    print("{:20}".format(fact(x)), end=" ")
    # print("{:20}".format(fact_save_1(x)))
    print("{:20}".format(fact_save_2(x)))

# -------------
# Пример вывода:

#   x               fact()          fact_save()
#   5                  120                  120
#  20  2432902008176640000 Traceback (most recent call last):
#   File "07_01_08_b.py", line 23, in <module>
#     print("{:20}".format(fact_save(x)))
#   File "07_01_08_b.py", line 15, in fact_save
#     assert x <= 15, "Не передавайте числа больше 15 во избежание переполнения памяти"
# AssertionError: Не передавайте числа больше 15 во избежание переполнения памяти
#
#   x               fact()          fact_save()
#   5                  120                  120
#  20  2432902008176640000 Traceback (most recent call last):
#   File "07_01_08_b.py", line 34, in <module>
#     print("{:20}".format(fact_save_2(x)))
#   File "07_01_08_b.py", line 24, in fact_save_2
#     raise ValueError("Не передавайте числа больше 15 во избежание "
# ValueError: Не передавайте числа больше 15 во избежание переполнения памяти