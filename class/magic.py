'''
bai 7 : magic Methods
'''

import math


class Point:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __str__(self):

        return f"({self.x}, {self.y})"

    def __repr__(self):

        return f"({self.x}, {self.y})"

    def __add__(self, other):

        new_x = self.x + other.x
        new_y = self.y + other.y

        return Point(new_x, new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Point(new_x, new_y)

    def __eq__(self, other):

        return self.x == other.x and self.y == other.y

    def __lt__(self, other):

        khoang_cach_self = math.sqrt(self.x**2 + self.y**2)

        khoang_cach_other = math.sqrt(other.x**2 + other.y**2)

        return khoang_cach_self < khoang_cach_other


if __name__ == "__main__":

    p1 = Point(3, 4)
    p2 = Point(1, 2)
    print(p1)
    print(repr(p1))
    print(p1 + p2)
    print(p1 - p2)
    print(p1 == p2)
    print(p2 < p1)
