while True:
    print("************************")
    print("~~~ Добро пожаловать ~~~")
    print("************************")
    a = int(input("Введите 1-е число: "))
    b = int(input("Введите 2-е число: "))
    c = input("Введите действие: ")
    try:
        if (c == "*"): print (a*b)
        if (c == "/"): print (a/b)
        if (c == "-"): print (a-b)
        if (c == "+"): print (a+b)
        if (c == "**"): print (a**b)
        if (c == "//"): print (a//b)
        if (c == "%"): print (a%b)
        if (c == "|"): print (a|b)
    except ZeroDivisionError:
        print("Число не должно быть 0")
