# -*- coding: utf-8 -*-
"""
Динамическое программирование.
Задача 3 (Задача о куче). Из камней весом p (i 1, ,N) i  набрать кучу весом ровно W или,
если это невозможно, максимально близкую к W (но меньшую, чем W). Все веса камней и значе-
ние W – целые числа.
"""
WMAX = 8
P = [2, 4, 5, 7]
NStones = len(P)

T = []
for i in range(NStones):
  T.append([0] * (WMAX + 1))
for w in range(P[0],WMAX+1):
  T[0][w] = P[0]

def showTable ( P, T ):
  print ( "   ", end="");
  for w in range(WMAX+1):
    print ( "{:3d}".format(w), end="")
  print("\n---", end="")
  for i in range(WMAX+1):
    print("---", end="")
  print()
  for i in range(NStones):
    print( "{:2d}:".format(P[i]), end="");
    for w in range(WMAX+1):
      print( "{:3d}".format(T[i][w]), end="" )
    print()
  print()

for i in range(1,NStones):
  for w in range(1,WMAX+1):
    t0 = T[i-1][w]
    if w >= P[i]:
      t1 = T[i-1][w-P[i]] + P[i]
      T[i][w] = max(t0, t1)
    else:
      T[i][w] = t0

showTable(P, T)

print("Оптимальное решение: w =", T[NStones-1][WMAX] )
print("Берем камни: ");
i = NStones-1
w = WMAX
w0 = T[NStones-1][WMAX]
while w0 > 0:
  while i >= 0 and T[i][w] == w0:
    i -= 1
  if i < 0:
    print ( w0 )
    break;
  print ( P[i+1], ' ', end="");
  w0 -= P[i+1]
  w = w0

