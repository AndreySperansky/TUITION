"""Удаляем пустые значения из списка"""

targetList = 'Hello World'

targetList = [v for v in targetList if not v.strip()=='']
print(targetList)

# или
targetList = filter(lambda x: len(x)>0, targetList)
print(list(targetList))