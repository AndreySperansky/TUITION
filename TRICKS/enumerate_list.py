"""12. Нумерованные списки"""

for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)
# 0 a
# 1 b
# 2 c
"""
Для тех, кто уже знаком с enumerate, может оказаться новостью, 
что у функции есть второй аргумент, задающий начальное число:
"""


for i, item in enumerate(['a', 'b', 'c'], 1):
    print(i, item)
# 1 a
# 2 b
# 3 c

