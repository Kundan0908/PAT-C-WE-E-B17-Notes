# OOPs logic
# class
# object
# Inheritance
# Encapsulation
# Abstraction
# Polymorphism

# Inheritance -> A class can inherit methods from its parent class.
class Batch():

    def __init__(self,batch): # Batch.__init__(self,stu_batch)
        self.batch = batch

    def publish_batch(self):
        return f"The student is from batch {self.batch}"

class Student(Batch):
    def __init__(self,name, stu_batch):
        self.name = name
        self.batch = stu_batch
        # Batch.__init__(self,stu_batch)

    def publish_details(self):
        return f"{self.name} is the name of the student"


name = Student('Bhaskar','PAT-B17')
print(name.publish_details())
print(name.publish_batch())

batch = Batch('PAT-B17')


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