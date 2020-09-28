from random import randint
secret_num = randint(1, 100)
try_count =  1
max_count = 3
while try_count <= max_count:
    print("Попытка %d  из %d " %(try_count, max_count))
    user_num = int(input("Введите число от 1 до 100 :"))
    if user_num == secret_num:
        print("Вы угадали")
        break
    elif user_num < secret_num:
        print("Вы ввели слишком маленькое число")
    elif user_num > secret_num:
        print("Вы ввели слишком большое число")
    try_count += 1
else:
    print("Вы проиграли, загаданное число:  %d " % secret_num, end='')



