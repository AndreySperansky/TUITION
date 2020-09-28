'''
Задача 3. Изменение данных о товарах
Необходимо написать программу, которая будет работать с информацией о товарах, хранящихся на
складе. Определим, что все данные вводятся с клавиатуры.
Программа должна выводить всю текущую информацию о товарах. Они описываются номером на
складе и соответствующим количеством. Пока пользователь не введет 0, программа позволит
вносить изменения в сведения о товарах.
После изменений программа также выводит текущую информацию о товарах на складе.
Для описания товаров создадим собственную структуру. Ее полями будут номер товара на складе и
его количество. После этого создаем массив объектов – Товар.
Алгоритм работы программы:
1. Исходный массив товаров заполняется внутри программы;
2. Программа в цикле выводит всю информации о каждом объекте, содержащемся в массиве;
3. После создаем «бесконечный» цикл, внутри которого пользователь сможет по введенному
номеру товара менять о нем информацию;
4. Как только пользователь решит, что больше никаких изменений о товарах он вносить не
хочет, он вводит цифру 0. Срабатывает break ;
5. В итоге программа выводит всю информацию о товарах.
'''

goods = {
'1' : [ 'Core-i3-4330' , 9 , 4500 ],
'2' : [ 'Core i5-4670K' , 3 , 8500 ],
'3' : [ 'AMD FX-6300' , 6 , 3700 ],
'4' : [ 'Pentium G3220' , 8 , 2100 ],
'5' : [ 'Core i5-3450' , 5 , 6400 ]
}
for i in goods:
    print( "%s) %s - %d шт. по %d руб" % (i, goods[i][ 0 ], goods[i][ 1 ], goods[i][ 2 ]))
while 1 :
    n = input('Введите № товара или 0 для завершения: ')
    if n != '0' :
        qty = int(input('Введите Количество: '))
        goods[n][ 1 ] = qty
    else :
        break
for i in goods:
    print( "%s) %s - %d шт. по %d руб" % (i, goods[i][ 0 ], goods[i][ 1 ], goods[i][ 2 ]))