alist = ['1', '2', '3']
alist = map(int, alist)

print(alist)

print(list(alist))


"""
В python 2 map вернет список, но в третьей версии вернется объект - итератор. 
Соответственно все числа преобразуются в int.

"""