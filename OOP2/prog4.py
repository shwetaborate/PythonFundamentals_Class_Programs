# abstarct class
# Abstract Class
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


circle1 = Circle(5)
print(f"Area of circle is {circle1.area():.2f} and perimeter is {circle1.perimeter():.2f}")

rectangle1 = Rectangle(5, 8)
print(f"Area of circle is {rectangle1.area():.2f} and perimeter is {rectangle1.perimeter():.2f}")