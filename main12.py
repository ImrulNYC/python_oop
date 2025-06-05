class Person:
    
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __del__(self):
        print("Object is being deconstructed")
    

    def 

p=Person("Mike",25)

print(p.__dict__)
del(p)


