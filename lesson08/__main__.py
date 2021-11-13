import abc
import math


class Colorable(abc.ABC):
    @abc.abstractmethod
    def color(self):
        pass

    def __str__(self):
        return "Color"


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    def __str__(self):
        return "Shape"


class Rectangle(Shape):
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def area(self):
        return self.sideA * self.sideB


class Circle(Shape, Colorable):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def color(self):
        return "Yellow"

    def __str__(self):
        return "Circle : " + Colorable.__str__(self) + Shape.__str__(self)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class ColorSquare(Square, Colorable):

    def area(self):
        return Square.area()

    def color(self):
        return "Blue"


def printArea(figure: Shape):
    print(figure.area())


if __name__ == '__main__':
    rect = Rectangle(2, 3)
    print(rect.area())

    cicle = Circle(10)
    print(cicle.area())

    square = Square(4)
    print(square.area())

    figures = [rect, cicle, square, 1, "Hi"]
    for f in figures:
        if isinstance(f, Shape):
            printArea(f)
    print("**********************************")
    for color_f in figures:
        if isinstance(color_f, Colorable):
            print(color_f.__str__())
