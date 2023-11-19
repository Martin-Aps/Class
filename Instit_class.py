class Person:
    def __init__(self, name, age, id_number):
        self.name=name
        self.age=age
        self.id_number=id_number

class student(Person):
    def __init__(self, name, age, id_number, grade, counter=0):
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
  

student1=student("reza navabi", "21", "2321", "B.S",0)
student2=student("vahid shiraze", "25", "9854", "M.S",1)
print(student1.register_student())
print(student2.register_student())


       
    
    