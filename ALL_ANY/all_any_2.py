a = 100

condition_1 = a % 2 == 0
condition_2 = a > 50
condition_3 = a < 1000

print(all([condition_1, condition_2, condition_3]))
print(any((condition_1, condition_2, condition_3)), '\n')

a = 99

condition_1 = a % 2 == 0
condition_2 = a > 50
condition_3 = a < 1000

print(all([condition_1, condition_2, condition_3]))
print(any((condition_1, condition_2, condition_3)), '\n')

a = 1

condition_1 = a % 2 == 0
condition_2 = a > 50
condition_3 = a > 1000

print(all([condition_1, condition_2, condition_3]))
print(any((condition_1, condition_2, condition_3)), '\n')