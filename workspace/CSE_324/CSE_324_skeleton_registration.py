from CSE_324_course import Course
from CSE_324_skeleton_student import Student

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")
accounting = Course("Accounting")
art = Course("Art I")

test_student = Student("Jill", "Middle", "Sample")

test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)
test_student.add_course(accounting)
test_student.add_course(art)

test_student2 = Student("Bill", "Middle2", "Sample")

test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)
test_student2.add_course(accounting)
test_student2.add_course(art)

#TODO Add a third test student and assign them four classes
test_student3 = Student("Jack", "Middle3", "Sample")

test_student3.add_course(phys_ed)
test_student3.add_course(language)
test_student3.add_course(science)
test_student3.add_course(history)
test_student3.add_course(accounting)
test_student3.add_course(art)
#TODO Add all the test students to a list of your own creation
listOfStudents = [test_student, test_student2, test_student3]
#TODO print student_list
print(listOfStudents)
#TODO iterate over each of the students in the list and print their names and course schedules.
    #Each iteration should:
        #get,concatenate, and print the first and last name of the student
        #print all courses for that student
        #print a blank line between students
'''for this part you may need to review the other skeleton code to:
        - see how to get items from a list
        - see if there is code (like a function) in that file you can call in this file
        - verify that running this file gets you the correct output with information from that file
    Also, review syntax of pulling items from a list from other activities'''
    
for student in listOfStudents:
    print(str(student.get_last_name)+","+str(student.get_first_name())+"+"+str(student.get_middle_name()))
    for course in student.courses:
        print(course)

print("\n")