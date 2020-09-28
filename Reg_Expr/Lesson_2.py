'''
https://www.youtube.com/watch?v=fXFtVDT0gmQ&list=PLA0M1Bcd0w8w8gtWzf9YkfAxFCgDb09pA&index=2
'''

'''
Квантификаторы {m,n},+,*,?
m - минимальное число совпадений с выражением
n - максимальное число совпадений с выражением
'''

import re

text = "Google Gooogle Gooooooogle"
match = re.findall(r"Go{2,5}gle.", text)
print(match)
# ['Google ', 'Gooogle ']

text = "Google Gooogle Gooooooogle"
match = re.findall(r"o{2,5}", text)
print(match)
# ['oo', 'ooo', 'ooooo', 'oo'] - мажорный(жадный) квантификатор

text = "Google Gooogle Gooooooogle"
match = re.findall(r"o{2,5}?", text)
print(match)
# ['oo', 'oo', 'oo', 'oo', 'oo'] - минорный квантификатор

text = "Google Gooogle Gooooooogle"
match = re.findall(r"Go{3,}gle", text)
print(match)
# ['Gooogle', 'Gooooooogle']

# Проверка корректности номера телефона
text = "89277091660"
match = re.findall(r"8\d{10}", text)
print(match)
# ['89277091660']

text = "стеклянный стекляный"
match = re.findall(r"стеклянн?ый", text)
print(match)
# ['стеклянный', 'стекляный']

text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
match = re.findall(r"\w+\s*=\s*[^;]+", text)
print(match)
# ['author=Пушкин А.С.', 'title = Евгений Онегин', 'price =200', 'year= 2001']

text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
match = re.findall(r"(\w+)\s*=\s*([^;]+)", text)
print(match)
# [('author', 'Пушкин А.С.'), ('title', 'Евгений Онегин'), ('price', '200'), ('year', '2001')]

text = "<p>Картинка <img src='bg.jpg'> в тексте </p>"
match = re.findall(r"<img.*>", text)
print(match)
# ["<img src='bg.jpg'> в тексте </p>"] - проявление жадности, ищет до последнего символа '>'

text = "<p>Картинка <img src='bg.jpg'> в тексте </p>"
match = re.findall(r"<img.*?>", text)
print(match)
# ["<img src='bg.jpg'>"] - c использованием минорного режима

# или что то же самое
text = "<p>Картинка <img src='bg.jpg'> в тексте </p>"
match = re.findall(r"<img.{0,}?>", text)
print(match)
# ["<img src='bg.jpg'>"]

text = "<p>Картинка <img src='bg.jpg'> в тексте </p>"
match = re.findall(r"<img[^>]*>", text)     # отключение внутреннего символа '>'
print(match)
# ["<img src='bg.jpg'>"]

# проверка на наличие обязательного атрибута src в тэге img
text = "<p>Картинка <img src='bg.jpg'> в тексте </p>"
match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text)     #
print(match)
# ["<img src='bg.jpg'>"]

text = "<p>Картинка <img> в тексте </p>"
match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text)     #
print(match)
# []

text = "<p>Картинка <img src='bg.jpg' alt = 'картинка'> в тексте </p>"
match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text)     #
print(match)
# ["<img src='bg.jpg' alt = 'картинка'>"]













