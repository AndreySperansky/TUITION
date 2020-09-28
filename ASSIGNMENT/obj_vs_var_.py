L = [1, 2, 3]
M = L 				# M и L – ссылки на один и тот же объект
print(id(M))
# 10634744
print(id(L))
# 10634744


print(L == M)		 		# Одно и то же значение
#True
print(L is M) 				# Один и тот же объект
#True

L = [1, 2, 3]
M = [1, 2, 3] 		# M и L ссылаются на разные объекты
print(L == M)  			#Одно и то же значение
#True
print(L is M)  			#Но разные объекты
#False

a = 1
b = a
print(b)
# 1
print(id(a))
# 1633248432
print(id(b))
# 1633248432

a = 2
print(b)
# 1
print(id(a))
# 1633248448
print(id(b))
# 1633248432

del(a,b)

# print(a)
# NameError: name 'a' is not defined
# print(b)
# NameError: name 'b' is not defined
# *****************************************************************************************
print(('*' * 125))
# *****************************************************************************************

a = []
b = a
a.append('any')
print(b)
# ['any']
print(a)
# ['any']
print(id(a))
# 15287800
print(id(b))
# 15287800




