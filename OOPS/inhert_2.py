class person:
    def getdata(self):
        self.name = str(input("Enter the name = "))
        self.id = int(input("Enter the voter ID = "))

    def displayp(self):
        print("Name :", self.name)
        print("Voter id :", self.id)


class employee(person):
    def getdata(self): # override is having same function name on both parent and child class.
        super().getdata()
        self.post = str(input("Enter the post = "))
        self.salary = int(input("Enter the salary = "))

    def displaye(self):
        super().displayp()
        print("Designation :", self.post)
        print("Salary :", self.salary)


emp = employee()
emp.getdata()
emp.displaye()
