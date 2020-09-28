d = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
while True:
    try:
        i = int(input('Введите номер дня недели: '))
    except ValueError:
        print('Вы ввели не число!')
    else:
        print(d.get(i, 'Такого дня нет!'))
