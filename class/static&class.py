'''
bai 6 statc mehods & class methon
'''


class Mathutils:

    pi = 3.14

    def add(a, b):
        return a + b

    def miltiply(a, b):

        return a * b

    def is_prime(n):

        if n < 2:

            return False

        for i in range(2, int(n ** 0, 5) + 1):

            if n % i == 0:

                return False

        return True


def circle_area(cls, radius):

    return cls.pi * radius * radius


class Counter:

    count = 0

    def __init__(self):

        Counter.count += 1

    def get_count(cls):

        return cls.count

    def reset(cls):

        cls.count = 0


if __name__ == "__maim__":

    print("-------Mathutils-------")
    print(Mathutils.add(3, 5))
    print(Mathutils.multiply(4, 6))
    print(Mathutils.is_prime(7))
    print(Mathutils.is_prime(10))

    print("\n-----Counter-----")

    c1 = Counter()

    print(Counter.get_count())

    c2 = Counter()
    print(Counter.get_count())

    Counter.reset()

    print(Counter.get_count())
          
