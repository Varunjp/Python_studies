class student:
    def __init__(self):
        self.name=str(input("Enter name = "))
        self.roll=int(input("Enter the roll number = "))
    def display(self):
        print("Name :", self.name)
        print("Roll number :", self.roll)

class mark(student):
    def __init__(self):
        super().__init__(self.name,self.roll)
        self.sub1= int(input("Enter mark of sub1 = "))
        self.sub2 = int(input("Enter mark of sub2 = "))
        self.sub3 = int(input("Enter mark of sub3 = "))
    def display(self):
        super().display()
        print("The mark of sub1 =", self.sub1)
        print("The mark of sub2 =", self.sub2)
        print("The mark of sub3 =", self.sub3)
class grade(mark):
    def __init__(self):
        super().__init__(self.name, self.roll, self.sub1, self.sub2, self.sub3)
    def printgrade(self):
        super().display()
        t=self.sub1+self.sub2+self.sub3
        p=t/300*100
        if(p>=80):
            print("A grade")
        elif(p>=60):
            print("B grade")
        elif(p>=40):
            print("C grade")
        else:
            print("Failed")

cls = grade()
cls.printgrade()
