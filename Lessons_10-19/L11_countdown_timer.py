import time

# Using time module to wait one second in real-time when counting down from ten to zero

# Using range() function, starting from ten, counting backwards (-1 step) down to zero (technically 1 since end is exclusive) and display msg
for seconds in range(10, 0, -1):
  print(seconds)
  time.sleep(1) # Using time module to tell program to sleep for one second before executing block again
print("Happy New Year!!")