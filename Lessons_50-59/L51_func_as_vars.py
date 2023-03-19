def hello():
    print('Hello')

# Will treat the func Hello() as an object rather than a fucntion and prints location of hello() func in computer's memory
print(hello)

# we can assign the memory address of the hello() function to a variable
hi = hello

# and can even invoke the hello() function through that variable by adding parenthesis
hi()
hello()

# another example with print() function
write = print
write("Whoa! I can't belive this works this way too!")