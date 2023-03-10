from L40_car_class import Car

car_1 = Car('Toyota', 'Aqua', 2015, 'White')
car_2 = Car('Ford', 'Mustang', 2022, 'Red')

print(car_1.make)
print(car_2.year)

# Although car_1 and car_2 are different instances of Car object, they both have same class varirables by default
print(car_1.wheel)  # 4
print(car_2.wheel)  # 4


# can change class variables for an object by accessing it and reassigning a value to the variable
car_1.wheel = 2
print("\n"+str(car_1.wheel))  # 2
print(car_2.wheel)  # 4

print()
# can both access the value and change class variable for future Class objects by using the Class
print(Car.wheel)  # 4

Car.wheel = 1 # Changes all default Car's default 'wheel' Class variable to 1 wheel
car_3 = Car('Chevy', 'Corvette', 2021, 'Blue')

print(car_2.wheel)  # 1
print(car_3.wheel)  # 1