#polymorphism
#method overriding

class Vehicle:
    def __init__(self,name,color, price):
        self.name = name
        self.color = color
        self.price = price
    
    def show(self):
        print("Details: ", self.name, self.color, self.price)

    def max_speed(self):
        print("Vehicle max speed is 180")

    def change_gear(self):
        print("Vehicle chnage 4 gear")
    

class Car(Vehicle):
    #method overriding
    def max_speed(self):
        print("The speed of the car is as below")
        print("Car max speed is 240")

    #method overriding
    def change_gear(self):
        print("The gear box details are as follows: ")
        print("Car change 7 gears")

class Bike(Vehicle):
    def max_speed(self):
        print("The speed of the bike is as below:")
        print("Bike max speed is 120")

    #method overriding
    def change_gear(self):
        print("The gear box details are as follows: ")
        print("Bike change 5 gears")


car = Car("Kia", "Black", 700000)
car.show()
car.max_speed()
car.change_gear()

bike = Bike("Pulsar", "Silver", 100000)
bike.show()
bike.max_speed()
bike.change_gear()