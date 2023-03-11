# multi-level inheritance - when a derived (child) class inherits another Child class

class Organism:
    
    alive = True

class Animal(Organism):
    
    def eat(self):
        print('This animal is eating')

# Inherits both Animal(parent) and Organism (grand-parent) classes
class Dog(Animal):
    
    def bark(self):
        print('This dog is barking')

# Dog Object will be able to do all things from parent and GParent classes
dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
