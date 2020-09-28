"""Класс collections.deque()"""
"""В соответствии с документацией Python, 
deque – это обобщение стеков и очередей. 
Они являются контейнером замен для списка Python. 
Список оптимизирован под быстрые операции с фиксированной длиной. 
Наш deque поддерживает аргумент maxlen, который устанавливает границы для deque. 
В противном случае deque будет расти до произвольных размеров. 
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque. 
Если вам нужен быстрый случайный доступ, используйте list."""

import string
from collections import deque

# формируем очередь из элементов-заглавных букв
NEW_DEQUE = deque(string.ascii_uppercase)
print(NEW_DEQUE)

# итерируем очередь
for el in NEW_DEQUE:
    print(el, end=' ')
print()

# добавляем элемент в конец очереди
NEW_DEQUE.append('end')
print(NEW_DEQUE)

# добавляем элемент в начало очереди
NEW_DEQUE.appendleft('start')
print(NEW_DEQUE)

# перемещаем два элемента с конца очереди в начало
NEW_DEQUE.rotate(2)
print(NEW_DEQUE)


# перемещаем два элемента с начала очереди в конец
NEW_DEQUE.rotate(-2)
print(NEW_DEQUE)

NEW_DEQUE.pop()
print(NEW_DEQUE)

NEW_DEQUE.popleft()
print(NEW_DEQUE)

# deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', \
# 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

# deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', \
# 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'end'])

# deque(['start', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',\
# 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'end'])

# deque(['Z', 'end', 'start', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',\
# 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'])

# deque(['start', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',\
# 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'end'])

# deque(['start', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', \
#        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#
# deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', \
#        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])