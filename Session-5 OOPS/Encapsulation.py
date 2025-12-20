# Encapsulation is a oops concept that allows binding of data in a class and control the object accessibility.

class A:
    def __init__(self):
        self._a = 10  # Protected object are declared with single underscore'_'
        self.__b = 20 # Private variable / objects are declared with double underscore '__'
        self.c = 30   # Public variables / object are declared without underscore

    def get_value(self):
        return self.__b

class B(A):

    def get_value(self):
        self._a += 10
        return self._a

obj  = A()
obj2 = B()
print(obj2.get_value())



