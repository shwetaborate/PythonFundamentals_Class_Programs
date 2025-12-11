#modules

# built in modules
# import statement examples

import math
num = 9
print("Number - ", num, "Squareroot - ", math.sqrt(9))

# import
from math import sqrt, factorial, pow
num =4
print ("Number : ", num, " Squareroot : ", sqrt(num), "Factorial : ", factorial(num))

# import from and *
from math import *
print("Sqaureroot : ", sqrt(16))
print("Factorial : ", factorial (4))


# import custom module
print("*****************Custom Module************************")
import MathCalculator
print("Additon: ", MathCalculator.add(2,4))
print("Multiplication: ", MathCalculator.multiply(3,5))

from MathCalculator import add, find_square
print("Addition: ", add(2,4))
print("Square: ", find_square(12))

#using MathCalculator Module
from MathCalculator import *
print("Addition: ", add(2,4))

print("Substraction: ", subtract(10,3))


# custom package

from MathCalcPackage.MathCalc import add, subtract, multiply, find_square

print("*****************Custom package************************")

print("Addition: ", add(2, 4))
print("Multiplication: ", multiply(3, 5))
print("Square: ", find_square(12))
print("Subtraction: ", subtract(10, 3))



