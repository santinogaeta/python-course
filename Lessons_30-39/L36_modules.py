import messages # Now allows access to all the functions and variables in the messages module
# could also define module with nickname: 'import messages as msg'

#Alternatively can import a different way to specify which funcs, variable to import
from more_msgs import x,y,z,addition,subtract
# don't need to specify module when using these imports unlike the first method

messages.hello() # will call the hello function from the messages module
messages.bye()  # will call the hello function from the messages module
print(messages.number)

print()

print(x)
print(y)
print(z)
print(addition(x,y))
print(subtract(z,messages.number))

# help("modules") to see all other modules available to use via python library