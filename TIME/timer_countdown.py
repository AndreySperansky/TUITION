import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print('Hello, world!')



# import time
# from random import randint
# while True:
#     a = randint(1, 100)
#     b = randint(1, 100)
#     print(a, '+', b, '=')
#     start = time.time()
#     answer = int(input())
#     if time.time() - start >= 5:
#         print('Вы не успели')
#     else:
#         if answer == a + b:
#             print('Верно')
#         else:
#             print('Неверно')