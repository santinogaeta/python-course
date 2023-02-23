# while loop -  a statement that will execute its block of code as long as its condition remains true

name = ""

# will keep asking user for input until something is entered
while len(name) == 0 :
  name = input("What is your name?: ")

# None defines nothing/the absence of a value (as opposed to null which is more 'unknown value')
last_name = None

while not(last_name):
  last_name = input("What's your last name?: ")

print("Hello "+name+" "+last_name)