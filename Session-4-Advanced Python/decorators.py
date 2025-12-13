# Decorators allow us to add additional functionality to existing functions.
# They do not change the actual code, just add functionality.
# They take another function as an argument and return a new function with enhanced functionality.

def func1(vishnu):
    print("I am from function 1")
    def wrapper():
        print("I am from function 2")
        vishnu()
    return wrapper()

@func1
def new_func():
    print("I am a new function")

def callback():
    print("I am a callback function")

callback()