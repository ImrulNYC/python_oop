#function deco, class deco

#a deco function extends functionality of func

import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        #before 
        print('Start')
        result=func(*args,**kwargs)
        print('End')
        return result
    return wrapper


@start_end_decorator
def print_name():
    print('Alex')


print_name()


@start_end_decorator
def add5(x):
    
    return x+5


x=add5(10)
print(x)

print(help(add5))
print(add5.__name__)