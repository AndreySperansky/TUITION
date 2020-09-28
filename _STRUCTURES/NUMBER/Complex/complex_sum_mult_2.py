'''
В соответствии с математическими правилами, сумма и произведение определенных комплексных
чисел будет выглядеть так:
a + b = (a.x + b.x) + (a.y + b.y)i
a * b = (a.x * b.x - a.y * b.y) + (a.x * b.y + a.y * b.x)i
Для описания комплексных чисел создадим структуру данных. Она будет содержать два поля,
описывающих действительную и мнимую части.
'''

# Вариант 2. Определение собственного класса и перегрузка операторов:
class Cmplx :
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def __add__ (self, obj):
        self.sumax = self.x + obj.x
        self.sumay = self.y + obj.y
    def __mul__ (self, obj):
        self.multx = self.x * obj.x - self.y * obj.y
        self.multy = self.y * obj.x + self.x * obj.y
        
x = float(input())
y = float(input())
a = Cmplx(x,y)
x = float(input())
y = float(input())
b = Cmplx(x,y)
a + b
a * b
print( 'Сумма: %.2f+%.2fj' % (a.sumax, a.sumay))
print( 'Произв.: %.2f+%.2fj' % (a.multx, a.multy))