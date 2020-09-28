"""НАИМЕНЬШЕЕ ОБЩЕЕ КРАТНОЕ"""
"""Наименьшее число которое делится на те числа НОК которого нужно найти"""
"""LOWERST COMMON MULTIPLE"""

def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)

x = int(input("a= "))
y = int(input("b= "))

print("LCM: ", lcm(x, y))



