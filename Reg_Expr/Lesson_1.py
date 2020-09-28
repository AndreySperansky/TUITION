'''
https://www.youtube.com/watch?v=1SWGdyVwN3E&list=PLA0M1Bcd0w8w8gtWzf9YkfAxFCgDb09pA
'''
import re

text = "Карта map  и объект bitmap - это разные вещи"
match = re.findall("map", text)
print(match)
# ['map', 'map']

text = "Карта map  и объект bitmap - это разные вещи"
match = re.findall("\\bmap\\b", text)
print(match)
# ['map'] - выделяется только слово map

text = "Карта map  и объект bitmap - это разные вещи"
match = re.findall(r"\bmap\b", text)
print(match)
# ['map'] - выделяется только слово map

text = "еда, беда, победа, 55 5  bitmap"
match = re.findall(r"(еда)", text)
print(match)
# ['еда', 'еда', 'еда']

text = "еда, беда, победа, 55 5  bitmap"
match = re.findall(r"\(еда\)", text)
print(match)
# []

text = "(еда), беда, победа, 55 5  bitmap"
match = re.findall(r"\(еда\)", text)
print(match)
# ['(еда)']

# Символьный класс

text = "Еда, беду, победа, 55 5  bitmap"
match = re.findall(r"[еЕ]д[ау]", text)
print(match)
# ['Еда', 'еду', 'еда']

text = "Еда, беду, победа, 55 5  bitmap"
match = re.findall(r"[0-9]", text)
print(match)
# ['5', '5', '5']

text = "Еда, беду, победа, -5 55 5  bitmap"
match = re.findall(r"[^0-9]", text)
print(match)
# ['Е', 'д', 'а', ',', ' ', 'б', 'е', 'д', 'у', ',', ' ', 'п', 'о', 'б', 'е', \
# 'д', 'а', ',', ' ', '-', ' ', ' ', ' ', ' ', 'b', 'i', 't', 'm', 'a', 'p']

text = "Еда, беду, победа, -5 55 5  bitmap"
match = re.findall(r"[а-я]", text)
print(match)
# ['д', 'а', 'б', 'е', 'д', 'у', 'п', 'о', 'б', 'е', 'д', 'а']

text = "Еда, беду, победа, -5 55 5  bitmap"
match = re.findall(r"[а-яА-Я]", text)
print(match)
# ['Е', 'д', 'а', 'б', 'е', 'д', 'у', 'п', 'о', 'б', 'е', 'д', 'а']

text = "Еда, беду, победа, -5 55 5  bitmap"
match = re.findall(r"[a-z]", text)
print(match)
# ['b', 'i', 't', 'm', 'a', 'p']

text = "Еда, беду, победа, -5 55 5  bitmap"
match = re.findall(r"[a-z0-9]", text)
print(match)
# ['5', '5', '5', '5', 'b', 'i', 't', 'm', 'a', 'p']

text = "Еда, беду, победа, -5 55 5  bitmap"
match = re.findall(r"\d", text)
print(match)
# ['5', '5', '5', '5']

text = "Еда, беду, победа, -5 55 5  bitmap"
match = re.findall(r".", text)
print(match)

# ['Е', 'д', 'а', ',', ' ', 'б', 'е', 'д', 'у', ',', ' ', 'п', 'о', 'б', 'е', 'д', 'а', ',', ' ', '-', '5', \
# ' ', '5', '5', ' ', '5', ' ', ' ', 'b', 'i', 't', 'm', 'a', 'p']

text = "Еда, беду, победа, -5 55 5  bitmap"
match = re.findall(r"\w", text)
print(match)
# ['Е', 'д', 'а', 'б', 'е', 'д', 'у', 'п', 'о', 'б', 'е', 'д', 'а', '5', '5', '5', '5', 'b', 'i', 't', 'm', 'a', 'p']

text = "Еда, беда, победа, -5 55 5  bitmap"
match = re.findall(r"\w", text, re.ASCII)
print(match)
# ['5', '5', '5', '5', 'b', 'i', 't', 'm', 'a', 'p'] - ASCII  не считает русский шрифт символом слова

text = "Еда,  -5 55 5  bitmap"
match = re.findall(r"\W", text, re.ASCII)
print(match)
# ['Е', 'д', 'а', ',', ' ', ' ', '-', ' ', ' ', ' ', ' '] - ASCII  считает русский шрифт не символом слова

text = "0xf 0xa .0x5"
match = re.findall(r"0x[\da-fA-F]", text, re.ASCII)
print(match)
# ['0xf', '0xa', '0x5']

text = "0xf 0xa .0x5"
match = re.findall(r"0x[.\da-fA-F]", text, re.ASCII)
print(match)
# ['0xf', '0xa', '0x5'] - внутри символьного клвссв точка это точка

text = "0xf 0xa .0x5"
match = re.findall(r".0x[\da-fA-F]", text, re.ASCII)
print(match)
# [' 0xa', '.0x5'] - вне символьного класса точка это любой символ



text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
match = re.findall(r"(\w+)\s*=\s*([^;]+)", text)
print(match)
# ['author=Пушкин А.С.', 'title = Евгений Онегин', 'price =200', 'year= 2001']
# [('author', 'Пушкин А.С.'), ('title', 'Евгений Онегин'), ('price', '200'), ('year', '2001')]




