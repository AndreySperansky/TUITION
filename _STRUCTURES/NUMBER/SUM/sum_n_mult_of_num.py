""" Сумма и произведение цифр числа c else continue"""

a = abs(int(input("Введите целое число: ")))
sum = 0
mult = 1
while a > 0:
    digit = a % 10
    sum = sum + digit
    if digit != 0:
        mult = mult * digit
    else:
        continue
    a = a // 10
print("Сумма цифр: ", sum)
print("Произведение цифр: ", mult)

c = 3 // 10
print(c)