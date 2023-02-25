# index operator [] - gives access to a sequence's element (strings, lists, tuples)

name = 'Nino Pino'

# String[<index>] will take the char at <index> within the string that can be used
if name[0].islower():
    print('Letter is LowerCase')
else:
    print('Letter is actually UpperCase')

first_name = name[0:4].upper()  # Don't actually need the 0 (is zero by default)
print(first_name) # NINO

last_name = name[5:].lower()  # Don't need to specify the last index if going to end of string
print(last_name)  # pino

# Can access indices in reverse by using negative index, will start on the right-side of the string
last_char = name[-1]
print(last_char)  # 'o'