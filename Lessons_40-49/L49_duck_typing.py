# Duck Typing - concept where the class of an object is less imprtant than the methods/attributes
#                 class type is not checked if minimum methods/attributes are present

class Duck:
    
    def walk(self):
        print('This duck is walking')

    def talk(self):
        print('This duck is qwacking')

class Chicken:

    def walk(self):
        print('This chicken is walking')

    def talk(self):
        print('This chicken is clucking')     

# Will not contain walk() method to prove duck typing extent
class Bird:
    
    def talk(self):
        print('This bird is chirping')

class Person:
    # duck object being passed through must have a walk() and talk() method to be capture()
    def capture(self, duck):
        duck.walk()
        duck.talk()
        print('Person caught this duck')

person = Person()
duck = Duck()
chicken = Chicken()
bird = Bird()

person.capture(duck)

# Since Chicken class has a walk() and talk() method, although it's not a Duck, it has minimum requirements for capture() method so will no throw error
person.capture(chicken)

# Below will cause error since Python checks Bird class and see no walk() method, since within capture() needs object to have a walk() and talk() method
# person.capture(bird)
