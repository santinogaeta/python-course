# slicing - used to create a substring by extracting elements from another string
# Can be used by indexing[] or using the slice() function to create a new object of the sliced string

# <str>[start:stop:step] - starting index of where to start slicing <str>, stopping index when to stop (exclusive - need to end one index ahead from stopping char)
# <str>[0:10:2] - stepping index is 1 by default, other values indicate the step of including other characters (eg step 2 will count every second character)

# <str>[:4] - leaving start index empty will assume index[0]
# <str>[4:] - leaving ending index empty will assume to include everything after starting index[4]

name = "Nino Pino"

first_name = name[0:4]
last_name = name[5:9]
step_example = name[0::2]

print(first_name)
print(last_name)
print(step_example) # "Nn io" - created a substring out of every second character

# negative step will create a substring in reverse
reverse_string = name[::-1]
print(reverse_string)


# slice() function allows the same slicing parameters to be reuseable, works same as indexing however values seperated by commas
website1 = "http://google.com"
website2 = "http://wikipedia.com"

# can use negative index to count backwards from the right-side of the string (eg -4 is four chars from the last char of the string)
slice_object = slice(7,-4)
print(website1[slice_object])
print(website2[slice_object])
