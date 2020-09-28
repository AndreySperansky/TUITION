def rs(s):
    s = s.lower()
    signs = "?!. \'\"`,:;-_/()[]~"
    s_without_signs = ""
    for letter in s:
        if letter not in signs:
            s_without_signs += letter
    if s_without_signs == s_without_signs[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"
    #return s_without_signs


print(rs("Я иду с мечем, судия!"))
print(rs("А роза упала на лапу Азора!"))
print(rs("Вон у батыров своры  табунов"))
print(rs("Делу - тело, лету - лед"))