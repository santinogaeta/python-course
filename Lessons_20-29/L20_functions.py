# function = a block of code that is executed only when called / invoked

# def function_name(): - define a function with def, a unique name and parenthesis (if no arguments) then colon
def hello():
    print('Hello! ', end="")
    print("Have a nice day")

hello() # Hello! Have a nice day


# def function_name(args[]): - can state if function is expecting arguments to be passed in, to then use in block of code
def welcome(name):
    print('Welcome ' + name)

# sending a string arg to welcome() function
welcome('Nino') # Welcome Nino

# Can also pass thorugh variables into functions
nickname = "PaPino"
welcome(nickname) # Welcome PaPino

# function with multiple parameter
def greeting(first_name, last_name):
    print('Greetings, ' +first_name+ ' ' +last_name)

greeting('Nino', nickname)  # Greetings, Nino PaPino

# function with args of different data types
def introduction(first_name, last_name, age):
    print("Hi, I am "+first_name+" "+last_name+", and I am "+str(age)+"years old.")

age = 26
introduction('Nino', nickname, age) # Hi, I am Nino PaPino, and I am 26years old.