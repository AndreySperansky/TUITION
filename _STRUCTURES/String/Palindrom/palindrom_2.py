def palindrom(s:str):
    l_size = len(s)
    del_item = " ,?-.!"
    for k in del_item:
        s = s.replace(k, '')
    s = s.lower()
    for i in range(l_size // 2):
        if s[i] != s[-i - 1]:
            return "Не палиндром"
    return "Палинром"


print(palindrom("Я иду с мечем судия!"))
print(palindrom("А роза упала на лапу Азора!"))
print(palindrom("Вон у батыров своры  табунов"))
print(palindrom("Делу - тело, лету - лед"))