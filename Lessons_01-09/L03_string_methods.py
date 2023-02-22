# methods that can be used on strings

name = 'nino Pino'

# len(<str>) will return an int value representing the length of the string (including whitespaces)
print(len(name)) # returns 9

# <str>.find("<char>") will return an int value corresponding to the index of where the char specified is located within the String (-1 if not found)
print(name.find('P')) # returns 5

# <str>.capitalize() will return a String where the first char is capatilsed, and everything else is lower cased
print(name.capitalize()) # returns 'Nino pino'

# <str>.upper() will return a String where all chars are capatilised
print(name.upper()) # returns 'NINO PINO'

# <str>.lower() will return a String where all chars are now lower case
print(name.lower()) # returns 'nino pino'

# <str>.isdigit() returns a boolean if String can be converted into a digit (int)
num = '3'
num2 = '3.5'
print(name.isdigit()) # False because contains no digits
print(num.isdigit()) # True because contains 'int'
print(num2.isdigit()) # False because 3.5 is a 'float' data type

# <str>.isalpha() returns boolean if String contains only alphabetical letters (False if contains whitespaces)
firstName = 'Nino'
print(name.isalpha()) # should be False because whitespace
print(firstName.isalpha()) # True

# <str>.count('<char>') returns an int for the number of times that specified char appears within the str
print(name.count('o')) # returns 2

# <str>.replace('<char1>','<char2>') returns a string where ever instance within str of char1 is replaced with char2
print(name.replace('o','a'))

# print(<str>*<int>) will display the str an int number of times
print(name*3)

