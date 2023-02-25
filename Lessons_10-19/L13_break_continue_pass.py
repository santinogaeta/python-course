# Loop control statements - changes a loop execution from its normal sequence

# break - will terminate the loop entirely
# continue - skips to the next iteration of the loop
# pass - does nothing, acts as a placeholder


# while True loop will keep looping forever, waiting for User to input their name
while True:
  name = input("Enter your name: ")
  if name != "":
    break # if the condition above is met, then 'break' will exit the forever while loop


# Wanting to print out phone_number without dashes using 'continue'
phone_number = "123-456-789"

# iterate and print through each number, but if char is a dash, will continue and move to the next
for i in phone_number:
  if i == '-':
    continue
  print(i, end="")
print()


# 'pass' basically says there is no code to be executed here and will continue on
for i in range(1,21):
  if i == 13:
    pass
  else:
    print(i)

# As opposed to 'continue' where it will force the loop to start at the next iteration