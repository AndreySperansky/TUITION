L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

""" 1 [2, 3, 4]
    2 [3, 4]
    3 [4]
    4 []        """



L = [1, 2, 3, 4]
while L:
    front, *L = L       # Получить первый и остальные элементы
    print(front, L)     # без операции извлечения среза

L1 = [1, 2, 3, 4]
def mysum(L1): 														# Использует расширенную
    first, *rest = L1 													# операцию присваивания
    return first if not rest else first + mysum(rest) 					# последовательностей

print(mysum(L1))
