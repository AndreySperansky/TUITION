'''
https://www.youtube.com/watch?v=8eyyv10l_5E&list=PLA0M1Bcd0w8w8gtWzf9YkfAxFCgDb09pA&index=5
'''

'''
Объект re.match, методы re.search, re.finder, re.findall
'''
import re



text = "<font color=#CC0000>"
match = re.search(r"(\w+)=(#[\da-fA-F]{7})\b", text)
print(match)
# Если объект не нашелся
# None


text = "<font color=#CC0000>"
match = re.search(r"(\w+)=(#[\da-fA-F]{6})\b", text)
print(match)
# Если объект не нашелся
# <re.Match object; span=(6, 19), match='color=#CC0000'>

print(match.group(0))
# color=#CC0000

print(match.group(1))
# color

print(match.group(2))
# CC0000

print(match.group(0, 1, 2))
# ('color=#CC0000', 'color', '#CC0000')

print(match.groups())
# ('color', '#CC0000')

print(match.lastindex)
# 2     - подразумевается последний индекс group(2)

print(match.start(1))
# 6 - индекс буквы "c"  в строке

print(match.end(1))
# 11

print(match.end(2))
# 19

print(match.span(0))
# (6, 19)

print(match.span(1))
# (6, 11)

print(match.span(2))
# (12, 19)

print(match.endpos)
# 20

print(match.pos)
# 0

print(match.re)
# re.compile('(\\w+)=(#[\\da-fA-F]{6})\\b')

print(match.string)
# <font color=#CC0000>

match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match.groupdict())
# {'key': 'color', 'value': '#CC0000'}

print(match.lastgroup)
# value

print(match.expand(r"\1:\2"))
# color:#CC0000

print(match.expand(r"\g<key>:\g<value>"))
# color:#CC0000

text = "<font color=#CC0000 bg=#ffffff>"
match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match)
# <re.Match object; span=(6, 19), match='color=#CC0000'>

text = "<font color=#CC0000 bg=#ffffff>"
for match in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text):
    print(match)
# <re.Match object; span=(6, 19), match='color=#CC0000'>
# <re.Match object; span=(20, 30), match='bg=#ffffff'>

text = "<font color=#CC0000 bg=#ffffff>"
for match in re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text):
    print(match)

    # ('color', '#CC0000')
    # ('bg', '#ffffff')
    
