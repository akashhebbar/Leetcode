class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myname(self):
        return "test"


class Child(Person):
    def info(self):
        # Initialize name in the parent, but pass None for age
        print(super().myname())  # Retrieve the name using myname method


pobj = Person('Parent', 18)
cobj = Child("Jack", 25)
print(pobj.name)  # Output: Parent
