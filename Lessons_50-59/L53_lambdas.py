# Lambda functions - functions written in 1 line using lanbda keyword (like a shortcut to writing a whole func)
#                  - accepts any number of args, but only has one expression

# lambda <parameters>:expression

def double(x):
    return x*2
print(double(5))

half = lambda x:x/2
print(half(10))

multiply = lambda x,y:x*y
print(multiply(3,4))

add = lambda x,y,z:x+y+z
print(add(1,2,3))

full_name = lambda first_name,last_name: first_name+" "+last_name
print(full_name("Nino","Pino"))

# Try to check if someone is at least 18yrs old (lambda <params>:<Boolean> if <cond> else <Boolean>)
age_check = lambda age:True if age >=18 else False
print(age_check(40))