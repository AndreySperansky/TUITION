s = 'Hello, World! (Привет, Мир!)'

#sb = s.encode('ascii')
sb = s.encode('UTF-8')

print(sb)
print(type(sb))

s = sb.decode('utf-8')

print(s)
print(type(s))

