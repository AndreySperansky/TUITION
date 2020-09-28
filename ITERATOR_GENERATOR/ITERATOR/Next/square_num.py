def square_num(nums):
    for i in nums:
        yield(i**2)
sqr = square_num([1,2,3,4])
print(next(sqr))
# 1
print(next(sqr))
# 4

print(list(sqr))  # Распечатает с того места где остановился последний раз
# [9, 16]
print(list(sqr))  # Второй раз один и тот же итератор использовать нельзя
# []
print(list(square_num([1,2,3,4])))  # Нужно создавать его второй раз
# [1, 4, 9, 16]

