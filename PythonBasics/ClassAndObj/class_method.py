class Person:
    gender = "male"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def user_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

    @classmethod
    def get_gender(cls):
        print("Gender:", cls.gender)


obj = Person("Akash", 25)

Person.get_gender()
obj.user_info()
