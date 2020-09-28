numbers = [1, 5, 3, 5, 9, 7, 11]
# Сортировка по возрастанию

print(sorted(numbers))

# Сортировка по убыванию
print(sorted(numbers, reverse = True))

# Набор строк

names = ['Max', 'Alex', 'Rate',]

# сортировка по алфавиту

print(sorted(names))

# Город, численность населения

cities = [('Москва', 100000), ('Лас=Вегас', 500000), ('Астрахань', 20000)]

# Такая сортировка сработает по алфавиту

print(sorted(cities))

# как отсортировать по численности населения?

def sort_population(city):
	return city[1]

print(sorted(cities, key = sort_population))

# Lambda

print(sorted(cities, key = lambda city: city[1]))





