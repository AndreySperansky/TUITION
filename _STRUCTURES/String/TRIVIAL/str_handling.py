s='''Все лето мы пили водку. Вот как-то открываю дверь, а на пороге Чебурашка, весь такой пьяный-пьяный, и бутылка 
из кармана торчит'''
s=s.replace('пили', 'читали')
s=s.replace('водку','книги')
s=s.replace('пьяный','начитанный')
s=s.replace('бутылка','энциклопедия')
print(s)

mas = ['Это просто строка', 'http://yahoo.ru', 'Еще одна строка', 'http://mail.ru']
for x in mas:
    if(x[0:4]=='http'):
        print(x)

s = 'Это обычная строка а в ней адрес почты speransky@gmail.com'
words = s.split(" ")
for w in words:
    n = w.find('@gmail.com')
    if n != -1:
        print('В строке присутствует e-mail ' + str(w))
