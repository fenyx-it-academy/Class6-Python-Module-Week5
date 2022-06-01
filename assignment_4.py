class Person():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        return f"""The name of the costumer is {self.name}
The age of the costumer is {self.age}"""


class Student(Person):
    def __init__(self, name, age,section):
        super().__init__(name, age)
        self.section=section

    def display(self):
        return f"""The name of the student is {self.name}
The age of the student is {self.age}
The section of the student is {self.section}"""

person=Person("Emrah",30)
print(person.display())
print("**************************")
student=Student("Emrah",30,"Engineering")
print(student.display())