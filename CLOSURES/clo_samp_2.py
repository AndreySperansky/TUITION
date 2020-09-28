
#Closure

def test(param):
    
    def my_print():
        return param
    
    return my_print()

o = test('my_string')
print(o)