# -*- coding: utf-8 -*-
"""
 Динамическое программирование.
Количество программ исполнителя Утроитель
"""
print ( "Введите начальное и конечное числа:" )
N0, N = map(int, input().split())

K = [0]*(N+1)

K[N0] = 1
for i in range(N0+1,N+1):
  K[i] = K[i-1]
  if i % 3 == 0:
    K[i] += K[i // 3]

print ( "Количество программ ", K[N] )