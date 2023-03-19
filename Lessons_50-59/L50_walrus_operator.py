# walrus operator := - an assignment expression
#                    - assigns values to variables as part of a larger expression

happy = True
print(happy)

# alternatively if we tried print(happy = True) to compact code to one line, this isn't allowed since we're trying to assign a variable as part of an expression
# but by using the walrus operator
print(sad := False) # assigns False to sad variable and invokes print expression to print sad's value False

# another example - asking user for food on loop to put into a list
foods = list()
while True:
    food = input("What food do you like?: ")
    if food.lower() == 'quit':
        break
    foods.append(food)

print(foods)

# can save lines on this type of operation
drinks = list()
# parentheses to help define what is being assigned to variable (without parenthesis, value would be 'TRUE' instead of the user input)
while (drink := input('What drinks do you like? :')) != 'quit': # assigns user input to vairable and checks if not equal to 'quit' as the expression for while-loop
    drinks.append(drink)

print(drinks)