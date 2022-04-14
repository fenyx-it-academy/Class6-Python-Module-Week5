class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Person name : ", self.name)
        print("Person age = ", self.age)
    
class Student(Person):
    def __init__(self, name , age , section):
        Person.__init__(self,name, age)
        self.section = section
    
    def displayStudent(self):
        print("Student name : ", self.name)
        print("Student age = ", self.age)
        print("Student section = ", self.section)
    
P = Person("Tomas Wild", 37)
P.display()

S = Student("Albert", 23 , "Mathematics")
S.displayStudent()