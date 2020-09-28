f = open('1.txt')
ints = []
try:
    for line in f:
        ints.append(int(line))
        print(ints)
except ValueError:
    print('Это не число. Выходим.')
except Exception:
    print('Это что ещё такое?')
else:
    print('Всё хорошо.')
    print(ints)
finally:
    f.close()
    print('Я закрыл файл.')
    # Именно в таком порядке: try, группа except, затем else, и только потом finally.

#Это не число. Выходим.
#Я закрыл файл.