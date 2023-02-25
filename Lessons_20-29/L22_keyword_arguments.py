# keyword arguments - arguments preceded by an identifier when we pass them to a function, 
                    # where order of arguments doesn't matter, unlike postional arguments (we've been using so far)

def hello(first_name, last_name, age):
    print("Hi, I'm "+first_name+" "+last_name+" and I'm "+str(age))

# positional args example, order of args DOES matter
hello('Nino', 'Pino', 26)

# keyword args will identify which args stand for each parameter by preceding args with <paramenter_name>=<arg>
# will do hello() function but args out of order and will still print the way it should
hello(age=26, first_name='Nino', last_name='Pino')
