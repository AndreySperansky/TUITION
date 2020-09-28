'''
https://www.youtube.com/watch?v=z5ed1wQYTi4&list=PLA0M1Bcd0w8w8gtWzf9YkfAxFCgDb09pA&index=6
'''

'''
методы re.match, re.split, re.sub, re.subn, re.compile
'''
import re

text = "+7(123)456-78-90"
match = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(match)
# <re.Match object; span=(1, 17), match='+7(123)456-78-90'>


text = " +7(123)456-78-90"
match = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(match)
# None

text = " +7(123)456-78-90"
match = re.search(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(match)
# <re.Match object; span=(1, 17), match='+7(123)456-78-90'>

text = """<point lon="40.893"  lat="52.6374" />
<point lon="40.859"  lat="52.6361" />;   <point lon="40.893"  lat="62.651" />
<point lon="40.8676"  lat="52.6585" />, <point lon="40.8672"  lat="52.6626" />
"""

ar = re.split(r"[\n;,]+", text)
print(ar)

# ['<point lon="40.893"  lat="52.6374" />', '<point lon="40.859"  lat="52.6361" />', \
# '<point lon="40.893"  lat="62.651" />', '<point lon="40.8676"  lat="52.6585" />',\
# ' <point lon="40.8672"  lat="52.6626" />', '']


text = """
Москва
Казань
Тверь
Самара
Уфа
"""

list = re.sub(r"\s*(\w+)\s*", r"<option>\1</option> \n", text)
print(list)

# <option>Москва</option>
# <option>Казань</option>
# <option>Тверь</option>
# <option>Самара</option>
# <option>Уфа</option>

count = 0
def replFind(m): # объект Match из прошлого урока
    global count
    count +=1
    return f"<option value='{count}'>{m.group(1)}</option>\n"

list = re.sub(r"\s*(\w+)\s*", replFind, text)
print(list)

# <option value='1'>Москва</option>
# <option value='2'>Казань</option>
# <option value='3'>Тверь</option>
# <option value='4'>Самара</option>
# <option value='5'>Уфа</option>

list, total = re.subn(r"\s*(\w+)\s*", r"<option>\1</option> \n", text)
print(list, total)
# <option>Москва</option>
# <option>Казань</option>
# <option>Тверь</option>
# <option>Самара</option>
# <option>Уфа</option>
#  5


count = 0
def replFind(m): # объект Match из прошлого урока
    global count
    count +=1
    return f"<option value='{count}'>{m.group(1)}</option>\n"

rx = re.compile(r"\s*(\w+)\s*")     # Предварительная Компиляция шаблона
list, total = rx.subn(r"<option>\1</option>\n", text)   # Использование экземпляря класса Pattern
list2 = rx.sub(replFind, text)      # Использование экземпляря класса Pattern
print(list, total, list2, sep="\n")

# <option>Москва</option>
# <option>Казань</option>
# <option>Тверь</option>
# <option>Самара</option>
# <option>Уфа</option>
#
# 5
# <option value='1'>Москва</option>
# <option value='2'>Казань</option>
# <option value='3'>Тверь</option>
# <option value='4'>Самара</option>
# <option value='5'>Уфа</option>