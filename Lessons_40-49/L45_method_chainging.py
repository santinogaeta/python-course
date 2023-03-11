# method chaining - calling mutiple methods sequentially, each call performs and action on same object and returns self

# If a method does not have a return, after the method has been invoked it will return 'None'
# Therefore for method chaining, need to return self for all method so next method has an object to act on
class Car:
    
    def turn_on(self):
        print('You start the engine')
        return self
    
    def drive(self):
        print('You drive the car')
        return self
    
    def brake(self):
        print('You step on the brakes')
        return self

    def turn_off(self):
        print('You turn off the engine')
        return self

car = Car()
car.turn_on().drive().turn_off()
print()
car.brake().turn_off()
print()
# if chain gets too long, can enter a line break '\' and move next operation to next line
car.turn_on()\
  .drive()\
  .brake()\
  .turn_off()