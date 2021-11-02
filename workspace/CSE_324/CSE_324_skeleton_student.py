from CSE_324_course import Course

class Student:
    
    student_id = 0
    
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.courses = []
        self.student_id = Student.student_id
        Student.student_id += 1
    
    def __str__(self):
        str_registration = self.get_last_name()+","+self.get_first_name()+"\n"
        for course in self.courses:
            str.registration = str_registration+str(course)+"\n"            
        return str_registration

        
    def get_first_name(self):
        return self.first_name
        
    def get_middle_name(self):
        return self.middle_name
        
    def get_last_name(self):
        return self.last_name
        
    def get_student_id(self):
        return self.student_id
    
    def add_course(self, new_course):
        #return self.add_course
        self.courses.append(new_course)
        # TODO add code to append new_course to self.courses
        #print "Course not yet added, implementation needed."