def commas(N):
    """
    Форматирует целое положительное число N, добавляя запятые,
    разделяющие группы разрядов: xxx,yyy,zzz
    """
    digits = str(N)
    assert(digits.isdigit())
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result

digit = 1234567123
print(commas(digit))

# 1,234,567,123
