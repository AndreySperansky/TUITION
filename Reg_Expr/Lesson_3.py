'''
https://www.youtube.com/watch?v=W9CffcsYpAU&list=PLA0M1Bcd0w8w8gtWzf9YkfAxFCgDb09pA&index=3
'''

'''
Сохраняющие скобки и группировка
'''

import re

text = "lat = 5, lon=7"
match = re.findall(r"\w+\s*=\s*\d+", text)
print(match)
# ['lat = 5', 'lon=7']

# но этот же шаблон находит и такие значения
text = "pi = 5, a=7"
match = re.findall(r"\w+\s*=\s*\d+", text)
print(match)
# ['pi = 5', 'a=7']

# чтобы находились только ключи lat lon:
text = "lat = 5, lon=7 pi = 5, a=7"
match = re.findall(r"lat\s*=\s*\d+|lon\s*=\s*\d+", text)
print(match)
# ['lat = 5', 'lon=7']



# применение не сохраняющего ключа в группирующих скобках (?:  ) -первый (внешний) уровень
text = "lat = 5, lon=7 pi = 5, a=7"
match = re.findall(r"(?:lat|lon)\s*=\s*\d+", text)
print(match)
# ['lat = 5', 'lon=7']

# второй (внутренний) уровень
text = "lat = 5, lon=7 pi = 5, a=7"
match = re.findall(r"(lat|lon)\s*=\s*\d+", text)
print(match)
# ['lat', 'lon']

# для того чтобы увидеть оба уровня сохранения ставим скобки снаружи
text = "lat = 5, lon=7 pi = 5, a=7"
match = re.findall(r"((lat|lon)\s*=\s*\d+)", text)
print(match)
# [('lat = 5', 'lat'), ('lon=7', 'lon')]

text = "lat = 5, lon=7 pi = 5, a=7"
match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)
print(match)
# [('lat', '5'), ('lon', '7')]

text = "lat = 5, lon=7 pi = 5, a=7"
match = re.findall(r"(lat|lon)\s*=\s*(?:\d+)", text)
print(match)
# ['lat', 'lon']

text = "<p>Картинка <img src='bg.jpg'> в тексте </p>"
match = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']>", text)
print(match)
# ['bg.jpg']

# Замена ' на "  результат не меняет
text = "<p>Картинка <img src='bg.jpg\"> в тексте </p>"
match = re.findall(r"<img\s+[^>]*src=[\"\'](.+?)[\"\']>", text)
print(match)
# ['bg.jpg']


text = "<p>Картинка <img src='bg.jpg\"> в тексте </p>"
match = re.findall(r"<img\s+[^>]*src=([\"\'])(.+?)\1>", text)
print(match)
# []

text = "<p>Картинка <img src='bg.jpg'> в тексте </p>"
match = re.findall(r"<img\s+[^>]*src=([\"\'])(.+?)\1>", text)
print(match)
# [("'", 'bg.jpg')]


text = "<p>Картинка <img src='bg.jpg'> в тексте </p>"
match = re.findall(r"(<img)\s+[^>]*src\s*=\s*(?P<name>[\"\'])(.+?)(?P=name)>", text)
print(match)
# [('<img', "'", 'bg.jpg')]

text = "<p>Картинка <img src='bg.jpg'> в тексте </p>"
match = re.findall(r"<img\s+[^>]*src=(?P<name>[\"\'])(.+?)(?P=name)>", text)
print(match)
# [("'", 'bg.jpg')]


with open("map.xml", "r") as f:
    lat = []
    lon = []
    for text in f:
        match = re.search(r"point\s+[^>]*?lon=([\"\'])(?P<lon>[0-9.,]+)\1\s+lat=([\"\'])(?P<lat>[0-9.,]+)", text)
        if match:
            v = match.groupdict()
            if "lon" in v and "lat" in v:
                lon.append(v["lon"])
                lat.append(v["lat"])

    print(lon, lat, sep="\n" )