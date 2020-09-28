# Разворот строк рекурсивным методом

from sys import argv
from time import time



nontrivial_rev1_call = 0 # counts number of calls involving concatentation, indexing and slicing
nontrivial_rev2_call = 0 # counts number of calls involving concatentation, len-call, division and sclicing

length = int(argv[1])



def rev1(l):
    global nontrivial_rev1_call

    if l == []:
        return []
    nontrivial_rev1_call += 1
    return rev1(l[1:])+[l[0]]

def rev2(l):
    global nontrivial_rev2_call
    if l == []:
        return []
    elif len(l) == 1:
        return l
    nontrivial_rev2_call += 1
    return rev2(l[len(l)//2:]) + rev2(l[:len(l)//2])



lrev1 = rev1(list(range(length)))
print ('Calls to rev1 for a list of length {}: {}'.format(length, nontrivial_rev1_call))


lrev2 = rev2(list(range(length)))
print ('Calls to rev2 for a list of length {}: {}'.format(length, nontrivial_rev2_call))  
print()

l = list(range(length))


start = time()
for i in range(1000):
    lrev1 = rev1(l)
end = time()

print ("Average time taken for 1000 passes on a list of length {} with rev1: "
       "{} ms".format(length, (end-start)/1000*1000))


start = time()
for i in range(1000):
    lrev2 = rev2(l)
end = time()

print ("Average time taken for 1000 passes on a list of length {} with rev2: "
       "{} ms".format(length, (end-start)/1000*1000))




