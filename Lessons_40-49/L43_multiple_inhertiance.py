# multiple inheritance - when a child class is derived from more than one parent class

class Prey:
    
    def flee(self):
        print('This animal flees')

class Predator:
    
    def hunt(self):
        print('This animal is hunting')

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# A child class with multiple inheritance is separated by a comma
class Fish(Prey,Predator):
    pass

# shows that a fish object has access to both Prey and Predator methods as their parents
fish = Fish()
fish.flee()
fish.hunt()