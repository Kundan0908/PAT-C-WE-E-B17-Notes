# Abstraction is a oops concept that allows hiding of a key functionality from outside call.

from abc import ABC,abstractmethod # import ABC class to use abstraction

class A(ABC):

    @abstractmethod
    def addition(self):
        pass
    
    def subtraction(self):
        pass

class B(A):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        total =  self.a + self.b
        return f"Summation value is {total}"

    def subtraction(self):
        total = self.a - self.b
        return f"subraction value is {total}"

obj = B(10,20)
print(obj.addition())
print(obj.subtraction())

obj2 = A()
print(obj2.subtraction())
