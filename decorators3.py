import functools

def repeat(num_times):
    def decorator_repeat(func):

        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeat

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        #before 
        print('Start')
        result=func(*args,**kwargs)
        print('End')
        return result
    return wrapper



def debug(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        args_repr=[repr(a) for a in args]
        kwargs_repr=[f"{k}={v!r}" for k,v in kwargs.items()]
        signature=", ".join(args_repr+kwargs_repr)
        print(f"calling {func.__name__}{signature}")
        result=func(*args,**kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator
def greet(name):
    greeting=f'Hello , :{name}'
    print(greeting)
    return greeting



greet('Alex')