# str.format() - optional method that gives users more control when displaying output

animal = 'cow'
item = 'moon'

# usual way to print a string while concatinating with other string
print('The '+animal+' jumped over the '+item)

# or by using <str>.format and using {} - format fields acting as placeholders to be replaced by a value or variable
print('The {} jumped over the {}'.format(animal, item))

# Can also state the index within a format field to specify the value/variable to pull from (positional argument)
print('The {1} jumped over the {0}'.format(animal, item))
print('The {0} jumped over the {0}'.format(animal, item)) # Can use these format field variables more than once


# Can also use keyword arguments pairs in the format() to specify within the format fields
print('The {animal} jumped over the {item}'.format(animal='Fox', item='log'))
print('The {animal} jumped over the {animal}'.format(animal='Fox', item='log')) # Can use these format field variables more than once

# Can use str.format with a variable containing a string
text = 'The {} jumped over the {}'
print(text.format(animal, item))

print()

# Using str.format() to add padding to the format field in place of the {}
name = 'Nino'

print('Hi, my name is {}. Nice to meet you'.format(name))

# {:int} or {:<int} - will add an <int> amount of padding to the RIGHT of the format field
print('Hi, my name is {:10}. Nice to meet you'.format(name))
print('Hi, my name is {:<10}. Nice to meet you'.format(name))

# {:>int} - will add an <int> amount of padding to the LEFT of the format field
print('Hi, my name is {:>10}. Nice to meet you'.format(name))

# {:^int} - will center the format field within the <int> number of padding spaces
print('Hi, my name is {:^10}. Nice to meet you'.format(name))

# if you have a positional or keyword arg and padding, format like {key:padding}
print('Hi, my name is {name:>15}. Nice to meet you'.format(name='Pino'))

print()

# Formatting numbers
number = 3.14159
big_number = 1000

# formatting how many numbers after decimal {:.<int>f} - will also round the number
print('The number pi is {:.2f}'.format(number))

# automatically placing a comma in a big number with {:,}
print('The number is {:,}'.format(big_number))

# display the number in binary with {:b}
print('The number is {:b}'.format(big_number))

# display the number in octal with {:o}
print('The number is {:o}'.format(big_number))

# display the number in hexadecimal with {:x} or {:X}
print('The number is {:x}'.format(big_number))
print('The number is {:X}'.format(big_number))

# display in scientific notation with {:e} or {:E}
print('The number is {:e}'.format(big_number))
print('The number is {:E}'.format(number))
