# Static value input
class person:
    def __init__(self, n, v):
        self._name = n
        self.id = v

    def displayp(self):
        print("Name :", self._name)
        print("Voter id :", self.id)


class employee(person):
    def __init__(self, n, v, s, d):
        super().__init__(n, v)
        self.post = d
        self.salary = s

    def displaye(self):
        print(self._name)  # private value
        super().displayp()
        print("Designation :", self.post)
        print("Salary :", self.salary)


emp = employee("Varun", 5546, 85720, "Eng")
emp.displaye()
