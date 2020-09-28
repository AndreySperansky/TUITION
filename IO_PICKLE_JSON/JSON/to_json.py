import json

friends = [
	{'name': 'Max', 'age': 23, 'phones': [123, 234]},
	{'name': 'Leo', 'age': 33}
]

print(type(friends))

# преобразуем список друзей в json
json_friends = json.dumps(friends)

print(json_friends)
print(type(json_friends))

# <class 'list'>
# [{"name": "Max", "age": 23, "phones": [123, 234]}, {"name": "Leo", "age": 33}]
# <class 'str'>

# обратно из json  в объект
friends = json.loads(json_friends)

print(friends)
print(type(friends))

