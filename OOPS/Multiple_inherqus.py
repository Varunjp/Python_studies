# Luminar qus
class student:
    def getdata(self):
        self.name = str(input("Enter the name = "))
        self.roll = int(input("Enter the roll number = "))
        self.course = str(input("Enter the course = "))

    def Displaystudent(self):
        print("Name of student = ", self.name)
        print("Roll number = ", self.roll)
        print("Course = ", self.course)


class Test(student):
    def getmark(self):
        self.mark = int(input("Enter the mark(500) = "))

    def displaymark(self):
        print("Total written mark = ", self.mark)


class Sports:
    def getsportsmark(self):
        self.sportsmark = int(input("Enter the sports mark(100) = "))

    def displaysportsmark(self):
        print("Mark gained on sports = ", self.sportsmark)


class Result(Test, Sports):
    def calculategrade(self):
        total = self.mark + self.sportsmark
        print("Total mark scored = ", total)
        if total >= 500:
            print("The gained grade = A")
        elif total >= 400:
            print("The gained grade = B")
        elif total >= 300:
            print("The gained grade = C")
        else:
            print("Failed")


res1 = Result()
res1.getdata()
res1.getmark()
res1.getsportsmark()
res1.Displaystudent()
res1.displaymark()
res1.displaysportsmark()
res1.calculategrade()
