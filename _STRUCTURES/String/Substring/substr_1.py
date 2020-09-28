"""В строке найти и заменить одну подстроку на другую. Если одинаковых подстрок несколько, заменить все."""

str = "Tree, box, chair, lamp, desk, cat, dog, grass, pig, box, lamp, shelf"
print(str)

subStrOld = input("Old substring: ")
subStrNew = input("New substring: ")
lenStrOld = len(subStrOld)

while str.find(subStrOld) > 0:
    i = str.find(subStrOld)
    str = str[:i] + subStrNew + str[i+lenStrOld:]


"""С комментариями:

# исходная строка
str = "Tree, box, chair, lamp, desk, cat, dog, grass, pig, box, lamp, shelf"
print(str)

# старая подстрока - заменяемая часть строки
subStrOld = input("Old substring: ")
# новая подстрока
subStrNew = input("New substring: ")
# длина старой подстроки
lenStrOld = len(subStrOld)

# Функция find() возвращает индекс первого символа
# подстроки. Если подстроки нет, то возвращает -1.
# Цикл используется на случай, если в строке
# несколько одинаковых подстрок.

while str.find(subStrOld) > 0:

    # сохранить в переменную индекс первого элемента
    # старой подстроки
    
    i = str.find(subStrOld)
    
    # Перезаписать строку: взять срез от начала до индекса,
    # добавить новую подстроки и соединить со срезом от конца
    # старой подстроки.
    
    str = str[:i] + subStrNew + str[i+lenStrOld:]

print(str)"""