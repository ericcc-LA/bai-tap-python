'''
bai 4 method overriding & super
'''


class Vehicle:

    def __init__(self, brand, model):

        self.brand = brand
        self.model = model

    def get_infor(self):

        return f"{self.brand} {self.model}"


class Car(Vehicle):

    def __init__(self, brand, model, doors):

        super().__init__(brand, model)

        self.doors = doors

    def get_info(self):

        return f"{self.brand} {self.model} , {self.doors}"

    def drive(self):

        return " car is driving"


class Motorcycle(Vehicle):

    def __init__(self, brand, model, type):

        super().__init__(brand, model)

        self.type = type

    def get_info(self):

        return f"{self.brand} {self.model} ({self.type})"

    def ride(self):

        return "Motorcycle is riding"


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 4)

    print(car.get_info())

    moto = Motorcycle("Harley", "Sportster", "cruiser")

    print(moto.get_info())
