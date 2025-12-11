#Hybrid inheritance
#super class
class Car:
    def car_wheel(self):
        print("This car has 4 wheels")

class BMW(Car):
    def model_info(self):
        print("This is a BMW car")

class Service(Car):
    def service_info(self):
        print("We have car service available")

class Showroom(BMW, Service):
    def availability(self):
        print("Currently we only have BMW models available")

showroom = Showroom()
showroom.availability()
showroom.model_info()
showroom.service_info()

