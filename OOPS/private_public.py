class account():
    def __init__(self):
        self.__bal = 0 # the data is now strongly private, without "_" data is public

    def deposit(self):
        self.dep = int(input("Enter the deposit amount = "))
        self.bal = self.bal + self.dep

    def withdraw(self):
        self.witd = int(input("Enter the amount to withdraw = "))
        if self.witd < self.bal:
            self.bal = self.bal - self.witd
        else:
            print("Insufficient amount")

    def enquire(self):
        print("Current balance is", self.bal)


a = account()
a.deposit()
a.withdraw()
a.enquire()
