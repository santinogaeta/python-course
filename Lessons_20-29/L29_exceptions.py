# Exceptions - events detected during execution that interrupt the flow of a program

# encase code that may potentially cause an error in a try: , except <type of exception>: to handle errors
try:
    numerator = int(input("Please enter a number: "))
    denomanator = int(input("Please enter another number to divide by: "))
    result = numerator / denomanator
except ZeroDivisionError:
    print("Cannot divide by zero")

#	Can also print the error as part of Error message
except ValueError as e:
    print(e)
    print("What was entered was not an integer")
# Good practice to specify specific exceptions like above, before adding general 'except Exception:' to cathc any you weren't anticipating
except Exception as e:
    print(e)
    print('Something else went wrong')
    
#	else statement so only print result if no errors occured
else:
    print(result)

#	finally: - will always execute this code at the end of a block no matter if Exception occured or not (good for file handling)
finally:
    print('This will always execute at the end')
    