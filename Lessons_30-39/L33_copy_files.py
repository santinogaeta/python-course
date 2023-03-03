import shutil # contains the three copy functions below

# shutil.copyfile() - copies the contents within the file, to destination file (can be new file)
shutil.copyfile('Lessons_30-39/text_doc.txt', 'Lessons_30-39/copy.txt')

# Alternatively with the same arguments there are two more copy functions:
# shutil.copy() - Does what copyfile() does AND copies permissions mode + destination can be a directory
# shutil.copy2() - Does what copyfile() + copy() does AND copies metadata (file's creation and modification times)