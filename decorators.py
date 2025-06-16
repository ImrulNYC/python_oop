##logging
from datetime import datetime
def logged(function):
    def wrapper(*args, **kwargs):
        value= function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f :
            fname=function.__name__
            print(f.write(f"{fname} return value {value}\n"))
            f.write(f"{fname} returned value {value} and time : {datetime.now()} \n")
        return value 
    
    return wrapper

@logged
def add(x,y):
    return x+y

print(add(10,20))

