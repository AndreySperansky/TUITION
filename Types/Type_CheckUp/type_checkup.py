my_str = 'Ура!'
if isinstance(my_str, str):
    print('Да, это строка')


num = 1.3
if isinstance(num, (int, float)):
    print('Да, это число')
else:
    print('Вы ыыели не число!')


num = 'c'
if isinstance(num, (int, float)):
    print('Да, это число')
else:
    print('Вы ввели не число!')