'''x=-5 
assert(x >= 0), 'x is not postive'
if x<0:
    raise Exception('x should be greater than 0')

def func():
    return None
'''
'''
try:
    a=5/0

except:
    print("an eror")
except Exception as e:
    print(e)
'''


try:
    a=5/1
    b=a+'b'
except ZeroDivisionError as d:
    print("Zero division", d)

except TypeError as e:
    print("Type error ",e)

else:
    print("everything is good")
finally:
    print("cleaning all ")


class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x>100:
        raise ValueTooHighError('value too high')
    
try:
    test_value(200)
except ValueTooHighError as e :
    print(e)