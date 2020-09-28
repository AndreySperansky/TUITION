import random

my_tuple = [[random.randint(1, 9) for _ in range(5)] for _ in range(7)]
for column in my_tuple:
    for item in column:
        print(item, end=' ')
    print()
    
# 5 X 7 означает 5 столбцов и 7 строк