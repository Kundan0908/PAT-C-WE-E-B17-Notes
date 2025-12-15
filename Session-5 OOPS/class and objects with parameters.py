"""Created Dog class with methods bark, sleep, description and behaviour"""
class Dog:
    legs = 4 # class argument

    def __init__(self,color,tail,specie): # __init__ is a constructor used for initializing an object
        self.color = color # object argument
        self.tail = tail
        self.specie = specie

    def bark(self):
        return "Dogs bark at everyone"

    def sleep(self):
        return "Dogs sleep for 10 hours a day"

    def description(self):
        return f"{self.specie} is a Dog with {__class__.legs} legs and is {self.color} with {self.tail} tail"

    def behaviour(self):
        return "They are friendly in nature"

doberman =Dog(color='black',tail='short',specie='Dobberman')
print(doberman.description())
shitzu = Dog (color='golden',tail='short',specie='shitzu')
print(shitzu.description())
print(shitzu.behaviour())


class Vehicle:
    # legs = 4 # class argument

    def __init__(self,vehicle,wheels): # __init__ is a constructor used for initializing an object
        self.wheels = wheels # object argument
        self.vehicle = vehicle

    def type_of_vehicle(self):
        return f'{self.vehicle} is a vehicle with {self.wheels} wheels'

vehicle_type = Vehicle('Bus',6)
print(vehicle_type.type_of_vehicle())
