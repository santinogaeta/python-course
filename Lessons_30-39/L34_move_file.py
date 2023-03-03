import os

source = 'Lesson_30-39/text_doc.txt'
destination = '/Users/santinogaeta/Desktop'

try:
    # since os.replace() will overwrite any file with same name at destination, check first
    if os.path.exists(destination):
        print('There is already a file with same name at destination')
    # os.replace(<source file/directory/folder>, <destination to move file to>) will move file from current place to destination
    else:
        os.replace(source,destination)
        print(source+" was moved")
# exception just in case Source file was not found
except FileNotFoundError as e:
    print(e)
    print(source+ " was not found")