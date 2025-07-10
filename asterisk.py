result=5*7
print(result)
result2=5**7
print(result2)

def foo(a,b,*args,**kwargs):
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key,kwargs[key])



my_tuple=(1,2,3)
mylist=[4,5,6]
myset={7,8,9}

new_list=[*my_tuple,*myset,*mylist]
print(new_list)