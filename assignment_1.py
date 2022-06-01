class School():
    
    students=[]

    def __init__(self,capacity):
        self.capacity=capacity
    
    def add_student(self,student):
        if self.capacity == len(self.students):
            print("Error! The capacity is full")
        else:
            self.students.append(student)
    
    def print_students(self):
        for i in self.students:
            print(i)

    

class Student():

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def __str__(self):
        return "Name: {} Age: {} Gender: {}".format(self.name,self.age,self.gender)

school=School(2)
student_1=Student("Emrah",30,"Male")
student_2=Student("Furkan",26,"Male")
student_3=Student("Aziz",35,"Male") 

school.add_student(student_1)
school.add_student(student_2)
school.add_student(student_3) 

school.print_students()
print(school.__dict__)

# student=Student("Emrah",30,"Male")  
# print(student)          