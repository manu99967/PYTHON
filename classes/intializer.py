
#initializer:constructor

#Special method in a class
#initializer: method is called whenever the blueprint is used
#To create an object
#method function is inside a class

#method your create you have to have the self: keyword

class Human():

    def __init__(self,gender,name):
        print("The initializer was called")
        
        self.gender=gender
        self.name=name
        if self.gender=="Male":
            self.ribs=24
            self.curse="Suffer"
        else :
          self.ribs=23
          self.curse="Pain"

    def another_one(self):
        print("This is another method")
    
adam=Human(name="adam",gender="Male") #object from a class
print("name",adam.name)
print("gender",adam.gender)
print("ribs",adam.ribs)
print("ribs",adam.curse)
print("")
eve=Human(name="eve",gender="Female")
print("name",eve.name)
print("gender",eve.gender)
print("ribs",eve.ribs)
print("curse",eve.curse)