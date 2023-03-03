# Read contents of a file line by line and print to console window

# with open(<file path>) - if text_doc.txt is in same folder, only need file name, otherwise full path needed like below
# Using with open(<file path>) - the file will close automatically once out of block of code, otherwise would have to close file manually
with open('/Users/santinogaeta/pythonFolder/python-course/Lessons_30-39/text_doc.txt') as file:
    print(file.read())

# If File is closed, this will print True. Otherwise if still open, this will print False
print(file.closed)

print() 

# Better practice to encase in try-catch in case of FileNotFoundError and handle it
try:
    with open('text_doc') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print('File was not found')