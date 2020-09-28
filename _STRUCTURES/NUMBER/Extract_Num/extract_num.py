# Внимание извлекает цифры а не числа

any_text = "hello3 bu 34 5kdf45"


list_num=[]
for i in any_text:
    try:
        num = int(i)
        list_num.append(num)
    except ValueError:
        continue
print(list_num)