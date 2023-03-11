# Inheritance - classes inheriting parent classes' attributes, methods etc

#	Parent class
class Animal:
    
    alive = True

    def eat(self):
        print('This animal is eating')

    def slumber(self):
        print('This animal is sleeping')    

#	Child class inheriting parent's attributes and methods, as well as having their own
class Rabbit(Animal):

		#	Unique method to Rabbit class
    def run(self):
        print('This rabbit is running')   
		#	Overrides the Parent class's eat() method when invoked
    def eat(self):
        print('The rabbit is eating a carrot')     

class Fish(Animal):
    
    def swim(self):
        print('This fish is swimming')

		#	Child class's unique method that will change Parent inherited attribute
    def cooked(self):
        self.alive = False
        print('This fish is now cooked and ready to eat!')

animal = Animal()
rabbit = Rabbit()
fish = Fish()

animal.eat()	#	This animal is eating
rabbit.eat()	#	The rabbit is eating a carrot
fish.swim()		#	This fish is swimming
print(fish.alive)		#	True
fish.cooked()		#	This fish is now cooked and ready to eat!
print(fish.alive)		#	False
fish.slumber()	#	This animal is sleeping