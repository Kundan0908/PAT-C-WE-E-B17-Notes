# OOPs -> Object oriented Programming

"""The below function is used for addition a given number with 10""" # Doc strings

def addition(num):
    return num + 10

num_1 = addition(10)
num_2 = addition(20)

# Advantages
# No repetition of code.
# Clean coding and proper alignment.
# Maintains code consistency.


# Classes and Objects
# classes are called a blueprint with which objects are created
# class contains methods
# class has a name

# Example 1
# ->  car is a concept for people to travel from one place to another place
# Method -> steering, wheels, gearbox, engine etc
# class have attributes which features like colors,alloy wheels,anti skid

# Example 2
# Dog are also type of a class
# Methods :  barking, sleeping, running, eating, body
# attribute : color

# Objects
# Object are the prototype which are called instance of a class.
# objects access methods of a class
# object have their own identity -> object has a unique name
# object have attributes , which could be behaviour or individual traits

# class Car:
#
#     def steering(self):
#         return "I am used to steer a car in a different direction"
#
#     def gearbox(self):
#         return "I am used to change gear of a car"
#
#     def engine(self):
#         return "I am used to provide power to the car"


class Dog:
    def bark(self):
        return "Dogs bark at everyone"

    def sleep(self):
        return "Dogs sleep for 10 hours a dat"

# print(Car().engine())
# print(Car().gearbox())

print(Dog().bark())

               # Class and Objects
class Car:

    def steering(self):
        return "I am used to steer a car in a different direction"

    def gearbox(self):
        return "I am used to change gear of a car"

    def engine(self):
        return "I am used to provide power to the car"


sedan = Car() # sedan is an instance of a class
print(sedan.steering()) # . operator will help to access methods of a class

suv = Car() # suv is an instance of a class
print(suv.gearbox()) #. operator will help to access methods of a class



