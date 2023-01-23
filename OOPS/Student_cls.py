class Student:
    def getdata(self, a, b, c):
        self.name = a
        self.age = b
        self.rollnumber = c

    def display(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Roll number : ", self.rollnumber)


std1 = Student()
std2 = Student()
std3 = Student()
std1.getdata("Anu", 18, 10)
std2.getdata("Sanu", 17, 14)
std3.getdata("Manu", 18, 12)
std1.display()
std2.display()
std3.display()
