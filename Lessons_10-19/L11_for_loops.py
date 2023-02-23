# for-loop - a statement that will execute its block of code for a limited amount of time

# range() - range function defines a range between numbers
# range(start,stop,step) - start (default 0) is inclusive of value, stop (exclusive, so needs +1 if including ending value), step (default 1) how much increment each time
for index in range(10) :
  print(index+1)
print("Finished first example")


for i in range(50,100+1,2):
  print(i)
print("Finished ex2")

#Can interate through anything iterable, including each char in a String
for c in "Nino Pino":
  print(c)
print("End of Ex3")