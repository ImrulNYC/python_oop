import time 

def timed(function):
    def wrapper(*args, **kwargs):
        
        before=time.time()
        value=function(*args,**kwargs)
        after=time.time()
        fname=function.__name__
        print(f" {fname} took {after-before} seconds")
        return value
    return wrapper

@timed
def myfuction(x):
    result=1

    for i in range(1,x):
        result*=i
    return result
(myfuction(1000))
