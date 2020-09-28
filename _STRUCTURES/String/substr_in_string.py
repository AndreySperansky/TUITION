"""Заменить подстроки в строке"""

things =    "tree, box, chair, lamp, \n" \
            "desk, cat, dog, grass, \n"  \
            "pig, box, lamp, shelf"

print(things + "\n")

old_item = (input('Old-item: '))
new_item = (input('New_item: '))
len_old_item = len(old_item)

i = things.find(old_item)  #Оператор find  возвращает индекс первого вхожждения или -1
while i > 0:
    before = things[:i]
    after = things[i + len_old_item:]
    things = before + new_item + after
    i = things.find(old_item)

print("\n" + things)
