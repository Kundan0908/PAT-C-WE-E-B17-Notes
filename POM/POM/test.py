class ABC:
    class_name = 'B16-B17'

    def __init__(self,name,age=22):
        self.name = name # object/instance variables
        self.age = age
#
obj1 = ABC('venkat')
obj2 = ABC('venkat',23)
print(obj1.age)
print(obj2.age)
