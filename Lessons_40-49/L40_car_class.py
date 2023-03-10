class Car:
    
    # class variable si declared inside the Class, but outside the Constructor
      # meaning all instances of Car variable will have the same Class variable by default
    wheel = 4 # all instances of Car objects will have four wheels by default

    # Variables declared inside Constructor are called 'Instance Variables'
    def __init__(self,make,model,year,colour):
        self.make =  make   # instance variable
        self.model = model    # instance variable
        self.year = year    # instance variable
        self.colour = colour    # instance variable