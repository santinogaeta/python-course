# if statements - condition block of code that will only execute if conditions are True

age = int(input("How old are you?: "))

# No brackets needed, set condition and end condition with a colon :, then proceed with the to-be-executed block of code
if age == 100:
  print("You're a century old")

# elif: - Else if - an additional specified condition if the above condition was not met
elif age >= 18:
  print("You are an adult")

elif age < 0:
  print("You haven't been born yet")

# else: for when above condition(s) are not met
else:
  print("You are a child")