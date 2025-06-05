class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"Hello, my name is {self.name} and age is {self.age} ")

    

person1=Person("Alice", 30)
person1.greet()

Person2=Person("Bob",22)
Person2.greet()