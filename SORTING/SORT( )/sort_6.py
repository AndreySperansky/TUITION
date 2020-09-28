from collections import Counter, deque

def foo(s):
    # Считаем уникальные символы.
    # Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})
    count = Counter(s)
    # Сортируем по возрастанию количества повторений.
    # deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
    #return sorted_elements[0]
    return sorted_elements

srn = 'Завтра День!'
print(foo(srn))