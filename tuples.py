#created in () , 

mytuple=("Max",)
print(type(mytuple))
for i in range(len(mytuple)):
    print(mytuple[i])

for i in mytuple:
    print(i)

mylist=list(mytuple)
mytuple_2=tuple(mylist)

a=(1,2,3,4,5,34,4)
b=a[2:4]
print(b)
print(a[::2])

newtuple="max",28,"boston"

name,age,city=newtuple
print(city)

i1,*i2,i3=a
print(i1)
print(i2)
print(i3)


