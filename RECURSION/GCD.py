""" НАИБОЛЬШИЙ ОБЩИЙ ДЕЛИТЕЛЬ (Алгоритм Евклида)"""
"""GREAT COMMON DEVISER"""


def gcd (a, b):
	if b == 0 :
		return a
	else:
		return gcd(b, a % b)
print(gcd( 5 , 15 ))






def gcd (a, b):
	if b == 0 :
		return a
	else :
		return gcd(b, a % b)
print(gcd( 5 , 8 ))



print(gcd( 5 , 15 ))
