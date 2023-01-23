class Vehicle:
    def getdata(self, n, a):
        self.name = n
        self.fuel_capacity = a

    def display(self):
        print("Name : ", self.name)
        print("Fuel_capacity : ", self.fuel_capacity)


car = Vehicle()
bike = Vehicle()
bus = Vehicle()
car.getdata("Alto", 40)
bike.getdata("Dominar", 20)
bus.getdata("Tata", 50)
car.display()
bike.display()
bus.display()
