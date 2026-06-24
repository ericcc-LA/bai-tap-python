'''
bai 5 properties
'''


class Rectangle:
    def __init__(self, width, height):

        self.width = width
        self.height = height

    def width(self):
        return self.__width

    def width(self, value):

        if value <= 0:
            return ValueError

        else:
            self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        if value <= 0:

            return ValueError
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


if __name__ == "__main":
    rect = Rectangle(5, 10)
    print(rect.area())
    print(rect.perimeter())

    rect.width = 8
    print(rect.area())

    rect.width = -5
    print(rect.width)
