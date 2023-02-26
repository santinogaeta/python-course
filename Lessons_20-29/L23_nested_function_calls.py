# nested fuction calls - functions calls inside other function calls (useful when nested functions return a value to use for outer functions)
# inner-most functions are called first

# Example - taking an user-input number, convert to float, find absolute and round to nearest whole number and print
num = input('Enter a number: ') # example: '-3.14'
num = float(num)  # -3.14
num = abs(num)  # 3.14
num = round(num)  # 3
print(num)  # 3

# Can do the above in nested function call
print(round(abs(float(input('Enter a number: ')))))
