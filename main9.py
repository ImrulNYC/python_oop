
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
    



car1=Car("ford","sedan",2025,4,4)

bike=Bike("Bmw","Mountain","2023",2)


print(car1.__dict__)
print(bike.__dict__)

car1.start()
bike.start()
