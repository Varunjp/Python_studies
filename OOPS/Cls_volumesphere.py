# Constructor is to initialise data

class sphere:
    def __init__(self):
        self.Rad = int(input("Enter the radius os sphere = "))

    def volume(self):
        from math import pi
        v = (4 / 3) * pi * self.Rad ** 3
        return v


sph = sphere()
print("The volume of give sphere is ", round(sph.volume(), 3))
