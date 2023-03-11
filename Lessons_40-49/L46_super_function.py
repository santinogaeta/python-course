# super() function - Function used to give access to the methods of a parent class
#                    Returns a temp  object of a parent class when used

class Rectangle:
    
    def __init__(self,length, width):
        self.length = length
        self.width = width

# Instead of copying Lines 7-8 into here, we use the super() function to use the parent's init() function
# super().<method in parent class wanting to use>(<any paramenters>)
class Square(Rectangle):
    
    #will access parent class's __init__ method and use its constructor will passed thorugh arguments
    def __init__(self,length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    
    #can also use the super().__init__(), but will still need to assign height since Rectangle class does not have height attribute
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

square  = Square(3,3)
cube = Cube(3, 3, 3)

print(str(square.area()))
print(str(cube.volume()))