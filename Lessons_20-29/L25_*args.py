# *args - parameter that will pack all arguments into a tuple
        # useful so that a function can accept a varying amount of arguments without needing to specify

# this function works fine only if there are exactly two arguments, if three passed through, cannot use this function
def add(num1, num2):
    return num1 + num2

# * - important for a form of packing, where we pack all arguments into a tuple
def addition(*args):
    sum = 0
    for i in args:
      sum += i
    return sum

# function addition() can now accept any number of args and perform the function
print(addition(4))
print(addition(4,2))
print(addition(4,5,7))
print(addition(4,2,3,6,8,6,2,6,12))

#important to note, cannot change args while in tuple, must change container
def subtraction(*nums):
   sum = 100
   nums = list(nums)  # chaning container from tuple into list (still ordered but now mutable)
   nums[0] = 20
   for i in nums:
      sum -= i
   print(sum)   

subtraction(5,50) # 30, since nums[0] was changed from 5 to 20 within function after changing from tuple to list