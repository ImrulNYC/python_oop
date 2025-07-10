def printname(name):
    print(name)

printname('Alex')


def foo(a,b,c):
    print(a,b,c)


foo(b=1,a=2,c=3)



def foo2(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    
    for key in kwargs:
        print(key, kwargs[key])


foo2(1,2,3,4,5, six=6,seven=7)
    
def foo3(a,b,*,c,d):
    print(a,b,c,d)

foo3(1,2,c=3,d=4)


def foo4(*args,last):
    for arg in args:
        print(arg)

    print(f"last {last}")

foo4(2,3,3,4,last=100)




def foo5(a,b,*c):
    print(a,b,c)


my_list=[0,1,2,4]

foo5(*my_list)

def foo6(a,b,c):
    print(a,b,c)


mydict={'a':1,'b':2,'c':3}

foo6(**mydict)


def foo7():
    global number
    x=number
    number=3
    print("number inside numer ", x)



number =0 


print(number)
foo7()
print(number)


def foo8():
    global number2 
    number2=8
    print("inside foo8", number2)

number2=5
print(number2)
foo8()

print(number2)
    


def foo9(x):
    global var
    x=6
    var=x
    print("inside foo9",x)



var=10
foo9(var)
print(var)