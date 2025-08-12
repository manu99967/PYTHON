class Car :
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def move(self):
            print("Drive")

class Bike :
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Ride")

class Plane :
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly")

car1 = Car("Toyota", "Corolla")
bike1 = Bike("Yamaha", "MT-07")
plane1 = Plane("Boeing", "747")

for x in (car1, bike1, plane1):
    x.move()
   
  
        