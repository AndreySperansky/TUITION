import decimal

name = "Fred"
print(f"He said his name is {name}.")
#'He said his name is Fred.'

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")  # nested fields
#'result:      12.35'


sec = int(input('Введите время в секундах: '))
h = sec // 3600       #отсекаем часы
m = (sec % 3600) // 60    #отсекаем минуты
s = (sec % 3600) % 60     #остались секунды

print(f'Текущее время: {h:{2}}:{m:{2}}:{s:{2}}')
result = f'{h:02}:{m:02}:{s:02}'
print(result)
