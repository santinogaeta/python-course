# Useful math functions located within the math module which we import in order to use
import math

pi = 3.14
negative_pi = -3.14
x, y, z = 1, 2, 3

# round(<float>) will round the variable up or down to the nearest whole number
print(round(pi))  # 3

# math.ceil(<float>) will round the value UP to nearest whole number
print(math.ceil(pi))  # 4

# math.floor(<float>) will round the value DOWN to the nearest whole number
print(math.floor(pi)) # 3

# abs(<float>) will return the absolute value of the variable (negative into positive)
print(abs(negative_pi))  # 3.14

# pow(<num1>,<num2>) will return the value of num1 to the power of num2
print(pow(pi,2))

# math.sqrt(<num>) will return the square root of the argument passed through
print(math.sqrt(pi))

# max([args]) will return the highest value of the arguments passed through
print(max(x,y,z)) # 3

# min([args]) will return the lowest value of the args passed through
print(min(x,y,z)) # 1