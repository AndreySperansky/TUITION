# Взято из "python_Self_Tution.pdf"  page45


print('Hello, {} !'.format('Vasya') + '\n')
print('{0} , {1} , {2} '.format('a', 'b', 'c')+ '\n')
print('{} , {} , {} '.format('a', 'b', 'c')+ '\n')
print('{2} , {1} , {0} '.format('a', 'b', 'c')+ '\n')
print('{2} , {1} , {0} '.format(*'abc')+ '\n')
print('{0} {1} {0} '.format('abra', 'cad')+ '\n')