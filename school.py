from unicodedata import name


class School:

    students = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
        else:
            print('School capacity is full. Cannot register:', student)

    def print_students(self):
        print(f"There are {len(self.students)} students. With following info:")
        for s in self.students:
            print(s)

class Student:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return "Student with name {} and gender {}".format(self.name, self.age)

school = School(2)
student_1 = Student("Eva", 21, "female")
student_2 = Student("Jack", 18, "male")
student_3 = Student("Anna", 18, "female")
school.add_student(student_1)
school.add_student(student_2)
school.print_students()
school.add_student(student_3)

print(school.__dict__)
print(student_1.__dict__)