# method overriding - when a child class overrides their inherited parent method within their class

class Animal:
    
    # method-signature
    def eat(self):
        print('This animal is eating')

# inherits Animal class methods
class Rabbit(Animal):
    
    # defining the eat() method again in child class overrides the parent class version of the method
    def eat(self):
        print('This Rabbit is eating a carrot')

animal = Animal()
rabbit = Rabbit()
animal.eat()  # This animal is eating
rabbit.eat()  # This Rabbit is eating a carrot