class Dog:


    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner


    def bark(self):
        print("whoof whoof")

class Owner:

    def __init__(self,name,address,phone):
        self.name=name
        self.address=address
        self.phone=phone

    

owner1=Owner("DANNY", " 123 SpringField", "123-456-7890")
owner2=Owner("jacob", " 331 SpringField", "0023-456-7890")


dog1=Dog("Bruce","Greyhound",owner1)

dog2=Dog("Freya","German",owner2)

