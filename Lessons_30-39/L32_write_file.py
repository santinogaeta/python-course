# with open(<file path>, 'w') as file: - to open a file to write into
# file.write(<string>)

text = "This is text that has been written from Lesson32 - how to write to files using python.\n"
try:  
    with open('Lessons_30-39/test.txt', 'w') as file:
        file.write(text)
        print('Text has been written into file')
except FileNotFoundError as e:
    print(e)
    print("File was not found")    

# if text was changed and program ran again with the same file, all text previously in file will be overwritten with new text
# this can be avoided by 'appending a file' using 'a', instead of 'w' for writting, in order to add to the file

addedText = 'This is text that is being appended from the same Lesson as above, to prove this is not overwritting what was written previously.'
try:  
    with open('Lessons_30-39/test.txt', 'a') as file:
        file.write(addedText)
        print('Text has been added into file')
except FileNotFoundError as e:
    print(e)
    print("File was not found")    