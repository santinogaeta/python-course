# return statement - functions that send values back to the caller

# define a return function by stating what to return at end of function
def multiply(num1, num2):
    result = num1 * num2
    return result

print(multiply(6,8))  # 48

# can also store return value ina variable
return_result = multiply(5,2)
print(return_result)  # 10

# more efficient way
def addition(num1, num2):
    return num1 + num2

