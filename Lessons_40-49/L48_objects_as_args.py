class Car:
    
    colour = None

class Motorbike:

    colour = None    

def change_colour(vehicle, colour):
    
    vehicle.colour = colour


car_1 = Car()
car_2 = Car()
car_3 = Car()
motorbike = Motorbike()

print(car_1.colour)
print(car_2.colour)
print(car_3.colour)

change_colour(car_1, 'red')
change_colour(car_2, 'white')
change_colour(car_3, 'yellow')
change_colour(motorbike, 'purple')

print()

print(car_1.colour)
print(car_2.colour)
print(car_3.colour)
print(motorbike.colour)