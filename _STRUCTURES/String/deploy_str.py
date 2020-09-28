first = input("Введите первую букву :")
last = input("Введите последнюю букву :")
newStr = ""
while first <= last:
    newStr += first
    first = chr(ord(first)+ 1)
print(newStr)
