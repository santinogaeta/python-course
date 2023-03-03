import os

# checking to see if a file exists on our computer

path = '/Users/santinogaeta/Desktop/textdoc.txt'

# os.path.exists(<path string>) - uses the os module to check if the path exists (doesn't check if file at end)
if os.path.exists(path):
    print('This file does exist')

    # os.path.isfile(<path string>) - checks if where the path leads ends up at a file
    if os.path.isfile(path):
        print('That is a file')

    # os.path.isdir(<path string>) - checks if where the path leads ends up at a directory
    elif os.path.isdir(path):
        print('This is a Directory')
        
else:
    print('This location does not exist')