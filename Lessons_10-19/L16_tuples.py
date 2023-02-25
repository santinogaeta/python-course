# tuple - collection which is ordered and unchangeable

# designate a tuple by using parentheses (), and listing items within
student = ("Nino Pino", 26, 'male')

# accessing information within using functions

# tuple.count(<item>) - will display how many times the <item> appears in the Tuple
print(student.count("Nino Pino"))

# tuple.index(<item>) - will return index that item lies in (Error if item is not in tuple)
print(student.index("male"))
