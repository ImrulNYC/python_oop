##lamda

add10= lambda x: x+10
print(add10(5))

multi=lambda x,y : x*y
print(multi(2,7))


point2D=[(1,2), (15,1), (5,-1),(10,4)
         ]
point2D_sort=sorted(point2D, key=lambda x:x[1])
print(point2D_sort)

def sort_by_y(x):
    return x[1]


#map(func,seq) 

a=[1,2,3,4,5]
b=map(lambda x: x*2,a)

d=filter(lambda x: x%2==0,a)
c=[x*2 for x in a]
print(list(d))

e=[x for x in a if x%2==0]


from functools import reduce
ab=[1,2,3,4,5,6] 

product_a=reduce(lambda x,y: x*y,a)
print(product_a)