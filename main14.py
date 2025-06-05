def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("I am decorating your function ")
        return_value= function(*args,**kwargs)
        return return_value
        

    return wrapper

@mydecorator
def hello_world(Person):
    print(f"hello -first {Person}")
    return f"hello  -second {Person}"

print(hello_world("mike"))