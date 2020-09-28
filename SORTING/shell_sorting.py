"""SHELL SORT"""
from random import randint

def shellSort(lst):
    gap = len(lst) / 2
    gap = int(gap)
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
#Sort the sub list for this gap
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j = j - gap
            lst[j] = temp

# Reduce the gap for the next element
        gap = int(gap / 2)

n = int(input("Введите длинну массива: "))
arr = []
for i in range(n):
    arr.append(randint(1, 99))
print(arr)
shellSort(arr)
print(arr)
