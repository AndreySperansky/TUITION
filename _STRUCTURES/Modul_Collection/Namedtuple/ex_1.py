'''Namedtuple позволяет создать тип данных, ведущий себя как кортеж. При этом каждому элементу
присваивается имя, по которому можно в дальнейшем получать доступ:'''
from collections import namedtuple


Pnt = namedtuple( 'Point' , [ 'x' , 'y' ])
p = Pnt(x= 1 , y= 2 )
print(p)
Pnt(x= 1 , y= 2 )
print(p.x)
print(p[ 0 ])

# Point(x=1, y=2)
# 1
# 1



Point = namedtuple('Point', ['x', 'y', 'z'])
p1 = Point(x=2, y=3, z=4)
