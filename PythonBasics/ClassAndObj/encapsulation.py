class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.model = model
        self.year = year

    def set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make


obj = Car('Ford', 'Mustang', 2018)
print(obj.get_make())
obj.set_make("BMW")
print(obj.get_make())
print(obj.model)
print(obj.year)
