
# создать список на букву А

names = ['Руслан', 'Дмитрий', 'Алексей', 'Андрей']

names = [name for name in names if name.startswith("А")]
print(names)
# ['Алексей', 'Андрей']