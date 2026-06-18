'''
bai 2 : ke thua
'''


class Animal:
    def __init__(self, name, species):
        self.name = name

        self, species = species

    def make_song(self):

        return "tieng keu"

    def eat(self):

        return f"{self.name} is eating"


class Dog(Animal):

    def __init__(self, name, breed):

        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self, item):
        return f"Dog fetches {item}"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"

    def scratch(self, target):
        return f"Cat scratches {target}"


if __name__ == "__main__":
    d = Dog("Lucky", "Golden Retriever")
    print(d.name)
    print(d.species)
    print(d.breed)
    print(d.make_sound())
    print(d.fetch("ball"))
    print(d.eat())

    c = Cat("Mimi", "black")
    print(c.make_sound())
    print(c.scratch("sofa"))
