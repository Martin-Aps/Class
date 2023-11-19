class Person:    #Parent Class
    def __init__(self, name, age, id_number):
        self.name=name
        self.age=age
        self.id_number=id_number

class Student(Person):        #Inherit from Person
    def __init__(self, name:str, age:int, id_number:int, grade:str, counter=0):
        super().__init__(name, age, id_number)
        self.grade=grade
        self.counter=counter

    def register_student(self):   
        if self.counter<2:
            new_student=f"Name: {self.name} - Age: {self.age} - Grade: {self.grade} - Student ID: {self.id_number}"
            self.counter+=1
            return new_student.title()
        else:
            return print("Class is Full")

class Course:
    def __init__(self, course_name:str, course_id:int):
        self.course_name=course_name
        self.course_id=course_id
    def course_list(self):
        new_course=f"Course ID: {self.course_id} - Course Name: {self.course_name}"
        return new_course

class Teacher(Person):
    def __init__(self, name:str, age:int, id_number:int, course:str, salary:int):
        super().__init__(name, age, id_number)
        self.course=course
        self.salary=salary
    def teachers_list(self):
        new_teacher=f"Name: {self.name} - Age: {self.age} - Course: {self.course} - Salary: {self.salary}"
        return new_teacher

student1=Student("reza navabi", "21", "2321", "B.S",0)
student2=Student("vahid shiraze", "25", "9854", "M.S",1)
print(student1.register_student())
print(student2.register_student())


# course1=Course("Mathematic", 12345678)
# print(course1.course_list())

# teacher1=Teacher("Ali Majidi", 47, 335566, "Mathematic", 10000)
# print(teacher1.teachers_list())

       
    
    