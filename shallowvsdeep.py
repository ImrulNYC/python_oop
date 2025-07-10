import copy

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
p1=Person("Alex",27)
p2=copy.copy(p1)

p2.age=28

print("p2",p2.age)
print("P1", p1.age)