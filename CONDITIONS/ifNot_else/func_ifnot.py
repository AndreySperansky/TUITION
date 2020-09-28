L1 = [1, 2, 3, 4]
def mysum(L1): 														# Использует расширенную
    first, *rest = L1 													# операцию присваивания
    return first if not rest else first + mysum(rest) 					# последовательностей

print(mysum(L1))

