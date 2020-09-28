try:
    x = 5
    if x < 10:
        raise ValueError('x should not be less than 10!')

except ValueError as err:
    print("Вы ввели неправильное число! \n", err)