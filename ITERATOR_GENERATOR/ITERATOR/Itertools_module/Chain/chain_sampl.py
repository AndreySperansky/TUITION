from itertools import chain
"""!"""
"""Функция chain() позволяет сделать итератор, состоящий из нескольких соединенных
последовательно итераторов. Итераторы задаются в виде отдельных аргументов. Пример:"""

it1 = iter([1,2,3])
it2 = iter([8,9,0])
for i in chain(it1, it2):
	print(i)