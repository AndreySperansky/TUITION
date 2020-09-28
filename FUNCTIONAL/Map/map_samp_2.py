old_list = ['1', '2', '3', '4', '5', '6', '7']

new_list = []
for item in old_list:
    new_list.append(int(item))

print(new_list)

#[1, 2, 3, 4, 5, 6, 7]

# то же но с функцией map

old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(map(int, old_list))
print(new_list)

#[1, 2, 3, 4, 5, 6, 7]