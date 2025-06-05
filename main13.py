class Vector:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self,other):
        return Vector(self.x+other.x, self.y+other.y)
    

    def __repr__(self):
        return f" X :{self.x}, Y : {self.y}"
    
    def __len__(self):
        return 0.0 
        ## for learning only
     
    def __call__(self):
        print("I was called")

v1=Vector(10,20)

v2=Vector(20,20)

v3=v1+v2

print(f"{v3.x}, {v3.y}")
