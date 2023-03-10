# Object Oriented Programming: Object is an instance of a class
# Classes - function as a blueprint that describes what attributes and methods each distinct object will have
  # Can create them in main module or separate file to import

# from <name of module> import <name of class>
from L39_car_class import Car

# To create an Object using class (must have __init()__ method) - define class() and input attributes within parentheses
car_1 = Car('Toyota', 'Aqua', 2015, 'White')
car_2 = Car('Ford', 'Mustang', 2022, 'Red')

print(car_1.make)
print(car_1.model)
print(car_2.year)
print(car_2.colour)
car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()
car_2.stop()