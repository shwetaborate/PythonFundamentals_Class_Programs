# Static methods - Example 1

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def product(x, y):
        return x * y

    @staticmethod
    def square(x):
        return x * x

# Calling static method directly on the class
result = MathOperations.add(10, 20)
print(f"Sum: {result}")      # Output: Sum: 30

result = MathOperations.square(5)
print(f"Square: {result}")   # Output: Square: 25