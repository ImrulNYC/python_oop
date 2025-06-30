#itertools : list, product,permu,combi, groupby, and infinite

from itertools import product

a=[1,2]
b=[3,4]
prod=product(a,b)
print(list(prod))

from itertools import accumulate
import operator
x=[1,0,6,3,4]
acc=accumulate(x,func=operator.mul)
acc2=accumulate(x,func=max)
print(list(acc2))

from itertools import groupby

a=[1,2,3,4,5]

def smaller_than3(x):
    return x<=3 
group_obj=groupby(a,key=smaller_than3)
for key,value in group_obj:
    print(key,list(value))


group_obj2=groupby(a, key=lambda x : x>2 )
for key,value in group_obj2:
    print(f" lamda-> {key},{list(value)}")


person=[{'name': 'Tim', 'age':25 },{'name':'Cat', 'age':25},
        {'name':'Jerry', 'age':5},{'name':'Jin', 'age':23}]


person_obj2=groupby(person,key=lambda x: x['age'] )
for key, value in person_obj2:
        print(key,list(value))


from itertools import count,cycle,repeat

for i in count(10):
     print(i)
     if i==15:
        break