"""5. Проверка на анаграммность
Проверить, являются ли строки анаграммами (например, в результате случайной перестановки букв)
поможет класс Counter модуля collections:"""

from collections import Counter

str1 = 'proglib'
str2 = 'prgolib'

print(Counter(str1) == Counter(str2))
print(Counter(str1))
print(Counter('p'))


# True
# Counter({'p': 1, 'r': 1, 'o': 1, 'g': 1, 'l': 1, 'i': 1, 'b': 1})
# Counter({'p': 1})