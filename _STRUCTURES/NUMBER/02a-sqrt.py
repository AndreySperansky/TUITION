# -*- coding: utf-8 -*-
"""
 
 Программа № 2a. Целочисленный квадратный корень 
 Вход: 
   нет 
 Результат: 
   123456788
   123456789
   123456789
"""
def isqrt(a):
  x = a
  while True:
    x1 = (x*x + a)//(2*x)
    if x1 >= x: return x
    x = x1

x = 123456789
print( isqrt(x*x-1) )
print( isqrt(x*x) )
print( isqrt(x*x+1) )