# nested loops - Loops within a loop (Can be mix between from and while)

rows = int(input("How many rows?: "))
cols = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
  for j in range(cols):
    print(symbol, end="") # end="" - prevents the cursor from moving down to next line when printing next iteration
  print()
