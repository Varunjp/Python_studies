# Constructor is to initialise data

class student:
    def __init__(self):
        self.Sub1 = int(input("Enter the mark of sub1 = "))
        self.Sub2 = int(input("Enter the mark of sub2 = "))
        self.Sub3 = int(input("Enter the mark of sub3 = "))

    def total(self):
        d = self.Sub1 + self.Sub2 + self.Sub3
        print("Total mark = ", d)
        return d


std1 = student()
std1.total()
