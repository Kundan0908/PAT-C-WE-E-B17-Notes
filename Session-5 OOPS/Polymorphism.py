# OOPs logic
# class
# object
# Inheritance
# Encapsulation
# Abstraction
# Polymorphism


# Polymorphism
class Vehicle:

    def vehicle_wheel(self):
        return f'All vehicles have wheels'

class Truck(Vehicle):

    def vehicle_wheel(self):
        return "Trucks have 8 wheels"

class Auto(Vehicle):

    def vehicle_wheel(self):
        return "Auto 3 wheels"

class Bike(Vehicle):

    def two_wheeler(self):
        print("I am a two wheeler vehicle")

vehicle1 = Truck()
print(vehicle1.vehicle_wheel())

vehicle2 =  Auto()
print(vehicle2.vehicle_wheel())

vehicle3 = Bike()
print(vehicle3.vehicle_wheel())

vehicle4 = Vehicle()
print(vehicle4.vehicle_wheel())