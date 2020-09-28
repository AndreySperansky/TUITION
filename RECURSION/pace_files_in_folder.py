import os

path = 'C:\\Java_Project'
print(path)

# print(os.listdir(path))
# for i in os.listdir(path):
    # print(i, path + '\\' + i, os.path.isdir(path + '\\' + i))
    # print(i, type(i), path + '\\' + i, os.path.isfile(path + '\\' + i))


def paceFile(path, level=1):
    print('Level = ', level, 'Content: ', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся', path + '\\' + i)
            paceFile(path + '\\' + i, level + 1)
            print('Возвращаемся в', path)
        
paceFile(path)
