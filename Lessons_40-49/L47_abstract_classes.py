# Abstract class - a class which contains one or more abstract methods
# (More of a template) - Prevents user from creating an object of that class but encourages to override abstract methods in a child class instead
# Abstract method - a method that has a declaration but does not have an implementation (needs to be overridden)

#	Needed for using abstract classes
from abc import ABC, abstractmethod

# Abstract class - template for children of Vehicle class (need parenthesis at end of Abstract Class eg 'class Vehicle()')
class Vehicle(ABC):
    
		# @abstractmethod - prevents a Vehicle object being created by mistake
		@abstractmethod
		def go(self):
				pass

		@abstractmethod
		def stop(self):
				pass

#	child classes need to implement all @abstractmethods
class Car(Vehicle):
    
	def go(self):
			print("You drive the car")
	
	def stop(self):
			print('Car stops')

class Motorcylce(Vehicle):
	
	def go(self):
			print("You drive the Motorcycle")
			
	def stop(self):
			print('Motorcycle stops')		

#	vehicle = Vehicle()	-	Will actually not create a vehicle object since it comes from abstract class with one or more @abstractmethod, cause error instead
car = Car()
motorcycle = Motorcylce()

#	vehicle.go()	#	Invalid since cannot create vehicle object
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()