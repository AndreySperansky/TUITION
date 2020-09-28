lst1 =[ 1 , 2 , 3 , 4 ]
lst=map(lambda x : x * 2 , lst1)
print(lst)
print(list(lst), '\n')

# [ 2 , 4 , 6 , 8 ]

t1 =(1 ,2 ,3)
t2 =( 5.0 , 6.0 , 7.0 )
t=map(lambda x , y : x / y , t1 , t2)
print(t)
print(list(t), '\n')


# [0.20000000000000001 , 0.33333333333333331 , 0.42857142857142855]
