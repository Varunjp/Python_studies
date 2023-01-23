class A:
    def __init__(self):
        self.a = int(input("Enter a = "))

    def display(self):
        print("A =", self.a)


class B:
    def __init__(self):
        self.b = int(input("Enter b = "))

    def display(self):
        print("B =", self.b)


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c = int(input("Enter c = "))

    def display(self):
        A.display(self)
        B.display(self)
        print("C =", self.c)

c1 = C()
c1.display()
