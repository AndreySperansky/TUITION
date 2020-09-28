import json

friends = [
	{'name': 'Max', 'age': 23, 'phones': [123, 234]},
	{'name': 'Leo', 'age': 33}
]

print(type(friends))


with open('friends.txt', 'w') as f:
	#  преобразуем список друзей в json и сохраняем в файл
	json_friends = json.dump(friends, f)

# обратно из файла в объект
with open('friends.txt', 'r') as f:
	friends = json.load(f)

print(friends)
print(type(friends))


