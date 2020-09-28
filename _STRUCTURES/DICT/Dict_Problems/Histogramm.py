"""Пример 1. Подсчитаем, сколько раз в строке встречается каждый символ:"""

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:d[c] = 1
        else:d[c] += 1
    return d
hist = histogram('how many times')
print(hist)

# {'a': 1,'e': 1,'i': 1,'h': 1,'m': 2,'o': 1,'n': 1,'s': 1,'t': 1,'w': 1,'y': 1}

"""Если нам нужно инвертировать данный словарь и в качестве ключа поставить частоту:"""

def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:inv[val] = [key]
        else:inv[val].append(key)
    return inv

print( invert_dict(hist))

# {1: ['h', 'o', 'w', 'a', 'n', 'y', 't', 'i', 'e', 's'], 2: [' ', 'm']}