""" Задание 1 СЕКУНДЫ --> ЧЧ.ММ.СС """

sec = input('Введите время в секундах: ')
if sec.isdigit():
    sec = int(sec)
    h = sec // 3600       #отсекаем часы
    m = (sec % 3600) // 60    #отсекаем минуты
    s = (sec % 3600) % 60     #остались секунды

print(f'Текущее время: {h:{2}}:{m:{2}}:{s:{2}}')
result = f'{h:02}:{m:02}:{s:02}'
print(result)


""" Задание 2 """

n = input('Введите целое число: ')
print(type(n))
n = int(n) + int(n + n) + int(n+ n + n)
print(type(n))
print(n)