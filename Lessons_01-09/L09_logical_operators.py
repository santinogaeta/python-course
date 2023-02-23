# Logical operators (and, or, not) - used to check if two or more conditional statements are True

temp = int(input("What is the temperature outside?: "))

# and - will make sure cond1 and cond2 are True before executing block of code
if temp >= 0 and temp <= 30 :
  print("The temperature seems good today")
  print("Go outside")

# or -as long as one of the conditionals is True, then the entire conditional statement is True and will exe the block of code
elif temp < 0 or temp > 30 :
  print("The temperature ain't ideal")
  print("Stay inside")

# not(<cond>) - will flip the boolean value from False -> True or vice versa
age = int(input("How old are you? :"))

if not(age > 21) :
  print("You can't drink in America")

else:
  print("Drink up!")