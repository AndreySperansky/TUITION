""" НАИБОЛЬШИЙ ОБЩИЙ ДЕЛИТЕЛЬ (Алгоритм Евклида)"""
"""GREAT COMMON DEVISER"""

a = int(input("введите a:"))
b = int(input("введите b:"))
while a!= 0 and b != 0:
    if a > b:
        a %= b
        print("a= ", a ,  "b= ", b, sep = " ")
    else:
        b %= a
        print("a= ", a ,  "b= ", b, sep = " ")

gcd = a + b
print(f"GCD {a} и {b} равно {gcd}")


# 2 Вариант

def gcd (a, b):
    if b == 0 :
        return a
    else :
        return gcd(b, a % b)
print(gcd( 5 , 15 ))



# 3 Вариант


def gcd (a, b):
    while a != b:
        if a > b:
            a = a - b
    else:
        b = b - a
    print (a)
gcd( 5 , 8 )