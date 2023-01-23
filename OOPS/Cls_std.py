class student:
    def getmark(self,a,b,c):
        self.Sub1=a
        self.Sub2=b
        self.Sub3=c
    def total(self):
        d=self.Sub1+self.Sub2+self.Sub3
        print("Total mark = ", d)

std1 = student()
std2 = student()
std1.getmark(88,96,97)
std2.getmark(90,96,99)
std1.total()
std2.total()

