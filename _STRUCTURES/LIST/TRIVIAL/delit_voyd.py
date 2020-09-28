"""Удаляем пустые значения из списка"""

targetList = 'Hello World'

targetList = [v for v in targetList if not v.strip()=='']
print(targetList)
# ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']


# или
targetList = filter(lambda x: len(x)>0, targetList)
print(list(targetList))

# ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']