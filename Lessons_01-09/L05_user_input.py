# input() allows the user to enter a value, that value can also be assigned
# input(<str>) <str> will appear when user is asked for input

name = input("What is your name?: ")

# If asking for int input, will need to do type casting BUT also must be a whole number

age = int(input("How old are you?: "))

# float type cast will accept numerical input with floating point

height = float(input("How tall are you in cm?: "))

print("Hello "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+"cm tall")