# dictionary - A changeable, unordered collection of unique key:value pairs (Maps of python?)

# defined by curly brackets {} and listing <Key>:<Value> pairs

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'New Zealand': 'Wellington',
            'Japan':'Tokyo'}

# dictionary[<Key>] - return the value associated with the <Key> in the dictionary, Error if <Key> has no <Value> in dictionary
print(capitals['New Zealand'])  # Wellington

# dictionary.get(<Key>) - returns value associated with <Key>, also lot safer to check since 'None' returns if no <Key>:<Value> pair
print(capitals.get('Japan'))  # Tokyo
print(capitals.get('Germany'))  # None

# dictionary.keys() - will return a list of all keys only
print(capitals.keys())  # dict_keys(['USA', 'India', 'New Zealand', 'Japan'])

# dictionary.values() - will return a list of all values only
print(capitals.values())  # dict_values(['Washington DC', 'New Dehli', 'Wellington', 'Tokyo'])

# dictionary.items() - will print out the entire dictionary containing all items
print(capitals.items()) # dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('New Zealand', 'Wellington'), ('Japan', 'Tokyo')])

# alternative way to print all items in <key,value> pairs
for key,value in capitals.items():
    print(key,value)  
# USA Washington DC
# India New Dehli
# New Zealand Wellington
# Japan Tokyo

# dictionary.update({<key1:value1>, <key2:value2>, ...}) - since dictionaries are mutable, can add new key:value entries to dictionary
capitals.update({'Germany':'Berlin'})
print('After updating with Germany: '+ str(capitals.items())) # dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('New Zealand', 'Wellington'), ('Japan', 'Tokyo'), ('Germany', 'Berlin')])

# Can also use dictonary.update({<existing_key>:<updated_value>}) to update existing keys with new values
capitals.update({'USA':'Las Vegas'})
print('After updating USA capital: '+ str(capitals.items()))  # dict_items([('USA', 'Las Vegas'), ('India', 'New Dehli'), ('New Zealand', 'Wellington'), ('Japan', 'Tokyo'), ('Germany', 'Berlin')])

# dictionary.pop(<key>) - will remove the key:value pair from the dictionary
capitals.pop('India')
print('After pop() India: '+ str(capitals.items())) # dict_items([('USA', 'Las Vegas'), ('New Zealand', 'Wellington'), ('Japan', 'Tokyo'), ('Germany', 'Berlin')])

# dictionary.clear() - will clear dictionary of all items
capitals.clear()
print('After clearing dictionary: '+ str(capitals.items())) # dict_items([])

