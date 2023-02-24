# 2D Lists - nested lists in lists

drinks = ['coffee', 'soda', 'tea']
dinner = ['pizza', 'burger', 'pasta']
dessert = ['cake', 'ice cream']

# Each item in foods-list is a list of its own items
food = [drinks, dinner, dessert]
print(food) # [['coffee', 'soda', 'tea'], ['pizza', 'burger', 'pasta'], ['cake', 'ice cream']]

# Accessing a specific list
print(food[1])

# Accessing specific item within specific list, add another index
print(food[1][2])