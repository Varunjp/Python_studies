# Single inheritance
class parent:
    def dislpayp(self):
        print("I am parent")


class child(parent):
    def displayc(self):
        # super().dislpayp()
        print("I am child")


child1 = child()
child1.dislpayp()
child1.displayc()

