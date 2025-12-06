# Defined block of code which is used to perform a specific task.
# Functions are defined in python with keyword 'def'
# Functions can have arguments.
# Functions can return value if needed
# a = 10
# b = 20
# print(a+b)
#
# a = 50
# b = 60
# print(a+b)
#
# a = 100
# b = 200
# print(a+b)

def empty_function():
    pass # 'pass' is used to functions which does not have ane specific activity, It completes body of a function and \
         #  used as null functions

def addition_of_two_numbers(a,b): # a and b are the arguments / inputs which are passed to a function
    return a+b # return is used to return value from a function
    # print (a+b) # printing values/statements on the console

x = int(input("Enter first value to be added: ")) # 10 -> '10' -> int('10') -> 10
# print(type(a))
# a = int(a) # Type conversion -> It is a way to convert data types of a variable
# print(type(a))

y = int(input("Enter second value to be added: "))
z = int(input("Enter third value to be added: "))


_total = addition_of_two_numbers(b=x,a=y)
print(f"The addition of {x} and {y} is {_total}")
_final_value = _total + z
print(f"Adding {_total} with {z} becomes {_final_value}")

