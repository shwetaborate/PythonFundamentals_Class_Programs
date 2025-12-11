#Class method for factory

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)
    
    def area(self):
        return 3.14 * self.radius ** 2
    
# creating an instance using a factory method

diam = float(input("Enter diameter: "))
circle = Circle.from_diameter(diam)

print(f'Circle radius: {circle.radius}')
print(f'Area: {circle.area()}')