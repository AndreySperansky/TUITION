# Удаление по ключу

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.pop("model")
print(thisdict, '\n')

# Удаление или произвольного элемента (не случайного)
thisdict =  {
"brand": "Ford",
"model":  "Mustang",
"year":  1964
}
thisdict.popitem()

print(thisdict, '\n')

# По ключу

thisdict =  {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
del thisdict["model"]
print(thisdict, '\n')

#Полностью

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
del thisdict
print(thisdict, '\n')

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.clear()
print(thisdict, '\n')