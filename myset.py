myset1={1,2,3,42,4}

print(myset1)
myset2={1,2,4,2}
print(myset2)

myset3=set()
myset3.add(2)
myset3.add(3)
myset3.add(4)
if 4 in myset3:
    myset3.remove(4)

print(myset3)


#frozen - immutable 

a=frozenset([1,2,3,4])
print(a)