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

# Multiple Inheritance -> A child class is deriving property from more than one parent class

class A:
    def __init__(self,a):
        self.a = a

class B:
    def __init__(self,b):
        self.b = b

class Addition(A,B):
    def __init__(self,a,b):
        A.__init__(self,a)
        B.__init__(self,b)

    def sum_of_numbers(self):
        total = self.a + self.b
        return f"The sum of a and b is {total}"

class Subtraction(A,B):
    def __init__(self,a,b):
        A.__init__(self,a)
        B.__init__(self,b)

    def sub_of_two_numbers(self):
        total = self.a - self.b
        return f"The sub of a and b is {total}"

obj = Addition(10,20)
print(obj.sum_of_numbers())

obj2 = Subtraction(10,20)
print(obj2.sub_of_two_numbers())

# Multilevel Inheritance -> More than one of level inheritance. A child class is a parent of another child class

class X:
    def __init__(self,x):
        self.x = x

class Y(X):
    def __init__(self,y):
        self.y = y

class Z(Y):
    def __init__(self,z,x,y):
        self.z = z
        X.__init__(self,x)
        Y.__init__(self,y)

    def get_all_values(self):
        return f"All defines values are {self.x},{self.y} and {self.z}"

obj3 = Z(1,2,3)
print(obj3.get_all_values())