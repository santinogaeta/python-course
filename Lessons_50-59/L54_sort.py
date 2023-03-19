# sort() method - used with lists
# sorted() function - used with iterables

students = ["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]

# sort method for lists will sort all items alphabetically
students.sort()
for pupil in students:
    print(pupil)

print()

# sort method also takes parameters eg sort(reverse=True) to sort in reverse alphabetical
students.sort(reverse=True)
for pupil in students:
    print(pupil)

print()

# If the list was instead an iterable (eg tuple), the sort() method for lists will not work
students_tuple = ("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")

# Instead with iterables we use the sorted() func
sorted_students = sorted(students_tuple)    # can also sort in reverse - sorted(student_tuple, reverse=True)
for pupil in sorted_students:
    print(pupil)

print()

# another parameter the sort() method can take is key - helpful when needing to sort by a specific element
# Here we have a list of tuples
student_info = [("Squidward","F",60),
                ("Sandy","A",30),
                ("Patrick","Z",25),
                ("Spongebob","B",31),
                ("Mr.Krabs","C",59)]

# to use the 'key' parameter, we need to pass through a function that will return the 'column' we want to sort by
# Eg sorting by grade, so by the index:1 of student_info
grade = lambda tuple:tuple[1] # will access the grades of each student and sort by those

# we pass in the lambda function to the key, to return what column to be sorting for 
student_info.sort(key=grade) #  Can also add reverse=True to sort backwards
for pupil in student_info:
    print(pupil)

print()

age = lambda tuple:tuple[2] # will access the grades of each student and sort by those

# we pass in the lambda function to the key, to return what column to be sorting for (this case: age)
student_info.sort(key=age,reverse=True) #  added reverse=True to sort backwards
for pupil in student_info:
    print(pupil)