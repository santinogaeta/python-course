# set - collection is unordered, unindexed, where there are no duplicate items allowed
# faster than lists if you need to check if an item is within a set


# set defined by listing items within curly-brackets {}
utensils = {"fork", "spoon", "knife", 'knife'}

# only one knife will appear in print since no duplicates
for item in utensils:
    print(item) # becuase unordered, potentially will have a different print order result each time

#set.add(<item>) - to add an item to the set
utensils.add('napkin')
print("After adding napkin: " + str(utensils))  # {'napkin', 'spoon', 'fork', 'knife'}

# set.remove(<item>) - to remove an item from the set
utensils.remove('fork')
print("After removing fork: " + str( utensils)) # {'napkin', 'spoon', 'knife'}

# set.clear() - clears set of all items
utensils.clear()
print("After clearing set: " + str(utensils)) # set()

utensils = {"fork", "spoon", "knife", 'knife'}
dishes = {"bowl", 'plate', 'cup', 'knife'}

# set1.difference(set2) - displays what does set1 have that set2 doesn't
print("Difference that utensils has that dishes doesnt: " + str(utensils.difference(dishes))) # {'spoon', 'fork'}
print("Difference that dishes has that utensils doesnt: " + str(dishes.difference(utensils))) # {'cup', 'plate', 'bowl'}

# set1.intersection(set2) - will return what both sets have in common
print("Common items in utensils and dishes set: "+ str(utensils.intersection(dishes)))  # {'knife'}

# set1.update(<set2>) - updates current set with the items from another set
utensils.update(dishes)
print("After updating utensils set with dishes set: " + str(utensils))  # {'knife', 'spoon', 'cup', 'fork', 'bowl', 'plate'}

# set1.union(<set2>) - can make a new set from a union of both set1 and set2
dinner_table = utensils.union(dishes)
print("After union of utensils and dishes set " + str(dinner_table))  # {'knife', 'spoon', 'fork', 'cup', 'bowl', 'plate'}


