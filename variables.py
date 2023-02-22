# variable - a container for a value

# String - a series of characters, defined within either double " " or single ' ' quotes
first_name = 'Nino'
last_name = "Pino"

# Will print the value associated with the variable
print(first_name)

# Since what is defined in print() is a String, will print out "firstName" instead of the value for firstName
print('firstName')

# Can print strings in conjuction will varables
print("Hello " + first_name)

# Can combine different values together as long as they're of the same data type
full_name = first_name + " " + last_name
print("Hello " + full_name)

# int Data Type
age = 21

# Changing int value in different ways
age = age + 1
print(age)
age += 1
print(age)

# Type casting an int into a String, to be used with other String data
print("Your age is: " + str(age))

# float DataType - floating point number: a number containing a decimal
height = 250.5
print("Your height is: " + str(height) + "cm.")

# boolean DataType - stores either True or False
human = True
print("Are you a human: " + str(human))
