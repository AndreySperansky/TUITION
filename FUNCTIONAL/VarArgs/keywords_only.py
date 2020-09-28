"""A byte of Python"""


def total(initial=5, *numbers, extra_number):
    """После параметра типа'*' (кортеж)  подразумевается только параметр типа '**' (словарь)
    даже если перед параметром      отсутствуют  две звездочки"""
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)
total(10, 1, 2, 3, extra_number=50)

#total(10, 1, 2, 3)
# Вызовет ошибку, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'.