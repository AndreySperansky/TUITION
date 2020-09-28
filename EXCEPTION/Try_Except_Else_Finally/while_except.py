NUM_A = None
# while type(NUM_A) != int:
while not isinstance(NUM_A, int):
    NUM_A = input("Введите целое число:\n ")
    try:
        NUM_A = int(NUM_A)
    except ValueError:
        print('Ошибка, нужно вводить целое число! \n')
D_SUM = 0
D_MULT = 1
while NUM_A > 0:
    DIGIT = NUM_A % 10
    D_SUM = D_SUM + DIGIT
    if DIGIT != 0:
        D_MULT = D_MULT * DIGIT
    else:
        D_MULT = D_MULT * 1
    NUM_A = NUM_A // 10
print("Сумма цифр: ", D_SUM)
print("Произведение цифр: ", D_MULT)
print(f"Сумма цифр: {D_SUM}")
print(f"Произведение цифр: {D_MULT}")