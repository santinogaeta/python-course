# Higher Order Functions - a function that either:
#                         a) accepts a function as an arg
#                         b) returns a function

# Example for (a)
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

# will receive a function as an argument 
def hello(func):
    text = func("Hello")
    print(text)

# invoking the higher-order function by passing in the name of function we want passed through
hello(loud) # HELLO

hello(quiet)  # hello

# Example for (b)
# nested function where divisor() returns the function dividend() as a variable (Lesson51)
def divisor(x):
    
    def dividend(y):
        return y / x
    
    # returns the function as a variable (L51)
    return dividend

# stores variable 2 in divisor, and divide is assigned the returned dividend function memory, so can be called by adding parenthesis to divide
divide = divisor(2)
# divide(10) basically invokes the dividend(10) function, and with the stored 2 for x, the function will return the ans to y/x
print(divide(10))