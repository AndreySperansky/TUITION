def mysum(L):                                       # Суммирует любые типы
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:]) # предполагает наличие  хотя бы одного значения

print(mysum([1]))
#   1
print(mysum([1, 2, 3, 4, 5]))
#   15
print(mysum(('s', 'p', 'a', 'm')))
#   ‘spam’
print(mysum(['spam', 'ham', 'eggs']))
#   ‘spamhameggs’

# mysum([]) будет завершаться ошибкой в 2 последних функциях
# Но они могут суммировать данные любых типов