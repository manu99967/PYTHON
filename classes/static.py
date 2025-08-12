

from datetime import datetime

def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f"{txt} \n")
       
#static<Not changing>
#static property:<Class itself> -> 
class Human():

    species="H.sapiens"
    genus="Homo"
    count=0
    
    def __init__(self,gender,name):
        print("The initializer was called")
        self._gender=gender
        self._name=name
        if self._gender=="Male":
            self._ribs=24
            self._curse="Suffer"
        else :
          self._ribs=23
          self._curse="Pain"
        #Human.count=Human.count+1
        self.__class__.count=self.__class__.count+1
    
    @property
    def name(self):
        now = datetime.now()
        print("Current date and time",now)
        write_file(f_name="log.txt",txt=f"At {now} got name from adam")
        return self._name
    
    @name.setter
    def name(self,new_name):
        # data integrity
        if not isinstance(new_name,str):
            print("Failed to update name")
            return
        #new_name is a string
        now = datetime.now()
        print("Current date and time",now)
        write_file(f_name="log.txt",txt=f"At {now} Name changed from {self._name} to {new_name}")
        self._name=new_name
        return new_name

    def print_self(self):
        print("----------------------")
        print("name",self._name)
        print("gender",self._gender)
        print("ribs",self._ribs)
        print("curse",self._curse)
        print("---------------------")


# adam=Human(name="adam",gender="Male") #object from a class
adam=Human(name="adam",gender="Male")
eve=Human(name="eve",gender="Female")

print("adam species",adam.species)
print("eve species",eve.species)
print("class property",Human.species)

print("Total humans",Human.count)
class HumanStatic(Human):
    """This class is used to demonstrate static properties and methods."""
    
    @classmethod
    def print_species(cls):
        """Prints the species and genus of the class."""
        print("Species:", cls.species)
        print("Genus:", cls.genus)
        print("Total count:", cls.count)
# Using the static method to print species and genus

class shape ():
    def __init__(self,name):
        self.name=name
        def describe(self):
            print(f"This is a shape named {self.name}.")


            class rectangle(shape):
                def __init__(self, width, height):
                    super().__init__("Rectangle")
                    self.width = width
                    self.height = height

               
            r1 = rectangle(5, 10)
            r1.describe()
            
            
    