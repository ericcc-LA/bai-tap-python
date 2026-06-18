class Person:
    def __init__(self, ten, tuoi, gioi_tinh):

        self.ten = ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh

    def getInfo(self):
        return "Ten: " + self.ten + " Tuoi: " + str(self.tuoi) + " Gioi Tinh: " + self.gioi_tinh

    def changeInfo(self, newName, newAge, newSex):
        self.ten = newName
        self.tuoi = newAge
        self.gioi_tinh = newSex


if __name__ == "__main__":

    my_self = Person("Quan", 23, "Nam")

    print(my_self.getInfo())

    my_self.changeInfo("Minh", 28, "Name")

    print(my_self.getInfo())
