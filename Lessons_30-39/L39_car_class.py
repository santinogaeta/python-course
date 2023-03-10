# Class naming convention - usually capalized
class Car:
    
    # def __init__(self) (initialiser) method is known as the 'Constructor'
    def __init__(self,make,model,year,colour):
        # Attributes - describe what a class has
        self.make =  make
        self.model = model
        self.year = year
        self.colour = colour

    # May also have methods within for Car objects
    # (self) means that the method will ahve a Car object passes into itself to be acted on
    def drive(self):
        print("This "+self.make+" is driving")

    def stop(self):
        print("This "+self.make+" has stopped")

# In python, (self) is passed in automatically when invoking method on that object