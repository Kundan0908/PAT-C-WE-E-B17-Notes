# A function is created to do a particular task
# Calling function with its name, activates the function execution

# callback function is a function which is passed as an argument

def greet(name):
    print(f"Hello!! {name}")

def my_function(f,name):
    print("Welcome to the class of callback function")
    f(name) #-> greet()

def addition(a,b):
    print(a+b) # 10+20

user_name = "Venkata"
my_function(greet,user_name)

# addition(10,20)