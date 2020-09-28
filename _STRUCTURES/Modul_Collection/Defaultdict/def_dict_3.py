from collections import defaultdict

animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'

print(animal['Nick'])  # Monkey

print(animal)
# defaultdict(<function <lambda> at 0x7f32f26da8c0>, {'Nick': 'Monkey', 'Sam': 'Tiger'})

"""
Здесь мы создали defaultdict, который назначает ‘Monkey’ в качестве значения по умолчания любому
ключу.Мы установили в ‘Tiger’, далее, следующий ключ мы не устанавливаем вообще. Если выведите второй ключ, вы
увидите, что он был назначен как ‘Monkey’.В случае, если вы еще  не поняли, практически невозможно вызвать ошибку
KeyError
"""

