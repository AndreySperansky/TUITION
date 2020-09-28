"""Поменять порядок цифр в числе на обратное"""

n = abs(int(input("Введите число: ")))
n_reversed = 0
while n > 0:
    digit = n % 10
    n = n // 10
    n_reversed *= 10
    n_reversed = n_reversed + digit
print("Реверсное число равно: ", n_reversed)




