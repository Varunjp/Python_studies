class rectangle:
    def readata(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        a=self.length*self.breadth
        print("Area is", a)

rect1 = rectangle()
rect2 = rectangle()
rect1.readata(10,5)
rect1.area()
rect2.readata(15,6)
rect2.area()
