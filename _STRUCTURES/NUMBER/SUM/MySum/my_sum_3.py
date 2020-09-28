def mysum(L):                                           # Использует расширенную
    first, *rest = L                                        # операцию присваивания
    return first if not rest else first + mysum(rest)

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
#  def mysum(first, * rest)      # работать не будет так как будет ожидать два отдельных аргумента