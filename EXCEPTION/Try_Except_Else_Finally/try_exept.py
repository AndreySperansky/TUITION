try:
    x = int(input("Введите целое число x (для вычисления 1/x): "))
    res = 1 / x

    print("1/{} = {:.2f}".format(x, res))
except Exception as err:
    print("Произошла ошибка!")
    print("Тип:", type(err))
    print("Описание:", err)

# --------------
# Примеры вывода:

# Введите целое число x (для вычисления 1/x): 3
# 1/3 = 0.33

# Введите целое число x (для вычисления 1/x): 5.5
# Произошла ошибка!
# Тип: <class 'ValueError'>
# Описание: invalid literal for int() with base 10: '5.5'