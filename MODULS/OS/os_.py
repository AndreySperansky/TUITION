import os

# имя операционной системы
print(os.name)

# текущая рабочая папка
print(os.getcwd())

# создаем новый путь
new_path = os.path.join(os.getcwd(), 'new_f')

# создаем папку по новому пути
os.mkdir(new_path)


