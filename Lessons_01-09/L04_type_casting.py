# Type casting - converting the data type of a value to another data type

x = 1
y = 2.0
z = '3'

print(x)  # int
print(y)  # float
print(z)  # string

x = str(x)
y = str(y)

print(x)  # int type cast into string
print(y)  # float type cast into string
print(type(x))
print(type(y))

x = float(x)
z = float(z)

print(x)  # int -> str type cast into float
print(z)  # str type cast into float
print(type(x))
print(type(z))

x = int(x)
z = int(z)
print(x)  # int -> str -> float type cast back into int
print(z)  # str -> float type cast into int
print(type(x))
print(type(z))

# Can't cast float -> string -> int, since int won't take a string with a floating point