a = [0]*10  # Stack means LIFO method
top = 0
x = int(input('введите число \n'))
while x!= 0:
    a[top] = x
    top += 1
    x = input('введите число \n')

    for k in range(10):
        print(a[k])




