import os
import shutil

# path to file we want to delete
file_path = 'Lessons_30-39/test.txt'
empty_dir_path = 'Lessons_30-39/empty_folder'
dir_path = 'Lesson_30-39/test_full_folder'

try:  
  # os.remove(<path to file) will remove the file
  os.remove(file_path)

  # os.rmdir(<path to empty directory>) will remove the EMPTY directory, as os.remove() will cause a PermissonError
  os.rmdir(empty_dir_path)

  # shutil.rmtree(<path to filled directory>) will rm directory with files in it, as os.rmdir() will cause OSError
  shutil.rmtree(dir_path) # considered dangerous since will delete all files within that directory too

# have remove functions within a try-catch in case target doesn't exist or unable to delete, and can handle the error
except FileNotFoundError as e:
  print(e)
  print("File already doesn't exist in path")
except PermissionError as e:
  print(e)
  print("You don't have permisson to delete this")
except OSError as e:
  print(e)
  print("You cannot delete a directory with files in it using that function")
else:
  print("Target was deleted")