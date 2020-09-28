import operator, functools

print(functools.reduce(operator.add, [2, 4, 6]))  # Оператор сложения в виде ф-ции
# 12
print(functools.reduce((lambda x, y: x + y), [2, 4, 6]))
# 12
