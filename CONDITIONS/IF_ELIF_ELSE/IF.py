number = 23
guess = int(input('Введите целое число \n >'))
if guess == number:
    print('Поздравляю, вы угадали')
    print('хотя и не выиграли никакого приза!')
elif guess < number:
    print('Нет, заданное число меньше этого')
else:
    print('Нет, заданное число больше этого')
print('Завершено')
