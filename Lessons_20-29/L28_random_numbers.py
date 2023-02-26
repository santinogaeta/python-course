import random # random module that will help simulate pseudo-randomness

# random.randint(num1,num2) - will generate a random number between num1 and num2
x = random.randint(1,6)
print(x)

# random.random() - will return a random floating number between 0 and 1
y = random.random()
print(y)

list = ['rock', 'paper', 'scissors']
# random.choice(collection) - generate a random choice from the list or collection of options
z = random.choice(list)
print(z)

# shuffle a list of items
cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
random.shuffle(cards)

print(cards)