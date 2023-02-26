# scope - the region that a variable is recognised, where it is only available inside the region it was created
# it si possible to have variables with the same name but with different scopes

name = 'Pino' # global scope - available inside and outside of functions

def display_name():
    name = 'Nino' # local scope - variable only recognisable inside this function
    print(name)


display_name()  # 'Nino' - from local scope in function
print(name) # 'Pino' - from global scope defined above
