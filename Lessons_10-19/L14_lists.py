# list - used to store multiple items in a single variable, designated by [item1, item2, ...]

food = ['pizza', 'apple', 'bread', 'jackfruit']

# can specify a single item within the list by targetting their index
print(food[1])  # will print 'apple'

# specifying indices can also be used to replace certain items
food[2] = 'toast'
print(food)

# using for loop to print all items in list
for item in food:
    print(item)

# list.append(<item>) - will add an item to the end of the list
food.append("ice cream")
# After appending 'ice cream': ['pizza', 'apple', 'toast', 'jackfruit', 'ice cream']

# list.remove(<item>) - will remove the speicifed item from list
food.remove("toast")
# After removing 'toast': ['pizza', 'apple', 'jackfruit', 'ice cream']

# list.pop() - will remove the last element in list
food.pop()
# After pop() last element: ['pizza', 'apple', 'jackfruit']

# list.insert(<index>, <item>) - will insert an <item> at specified <index> within list
food.insert(2, 'toast')
# After inserting 'toast' at index 2: ['pizza', 'apple', 'toast', 'jackfruit']

# list.sort() - will sort list alphabetically
food.sort()
# After sorting: ['apple', 'jackfruit', 'pizza', 'toast']

# list.clear() - will clear the list of all items
food.clear()
# After clearing list: []
