from MODULS import random_list
from MODULS.OS.mk_del_10_folders import create_folders, del_folders

create_folders()
del_folders()

print(random_list.get_random([2, 3, 5, 6, 8, 9]))
print(random_list.get_random([]))



