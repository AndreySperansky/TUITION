objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}
print(a_dict)

#{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}