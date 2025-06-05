#poly - many forms 


class Vehicle:
    def __init__(self,brand,model,year):

        self.brand=brand
        self.model=model
        self.year=year

    def start(self,speed=0):
       
        print("Vehicle is starting")
        print(f"top level", speed)

    def stop(self):
        print("stopping")


class Car(Vehicle):

    def __init__(self, brand, model, year,number_doors,number_whell):
        super().__init__(brand, model, year)
        self.number_doors=number_doors
        self.number_whell=number_whell

    def start(self,speed=10):
        
        print(f"car class", speed)


class Bike(Vehicle):

    def __init__(self, brand, model, year,number_whell):
        super().__init__(brand, model, year)
        self.number_whell=number_whell
    

class Ship(Vehicle):

    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

        
  



Vehicles=[
Car("ford","sedan",2025,5,4),
Bike("bmw","mountain",2024,2),

]

##loop 

for Vehicle in Vehicles:
    if isinstance(Vehicle,Car):
        print(f"inspecting {Vehicle.brand}, {Vehicle.model} , ({type(Vehicle).__name__})")
        Vehicle.start()
    elif isinstance(Vehicle,Bike):
        print(f"inspecting {Vehicle.brand}, {Vehicle.model} , ({type(Vehicle).__name__})")
        Vehicle.start()
    
    else:
        raise Exception("Object is not vehicle")