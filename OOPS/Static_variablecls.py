# Static variables
class Student:
    studentcount = 0

    def __init__(self, r, n):
        self.rollno = r
        self.name = n
        Student.studentcount += 1

    def displaycount():  # Static function
        print("Total strength of the class", Student.studentcount)

    def display(self):
        print("Name = ", self.name)
        print("Roll no = ", self.rollno)


S1 = Student(4, "Emil")
S2 = Student(5, "Derrik")
S3 = Student(6, "Ferrik")
S1.display()
print("********")
S2.display()
print("********")
S3.display()
print("********")
print(Student.studentcount)
Student.displaycount()
