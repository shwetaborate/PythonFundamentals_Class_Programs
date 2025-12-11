#Error Handling
'''
length = input("Please enter length: ")
breadth = input("Please enter breadth: ")
area = length * breadth
print("Area - ", area)
'''
'''
try:
    length = input("Please enter length: ")
    breadth = input("Please enter breadth: ")
    area = length * breadth
    print("Area - ", area)
except TypeError as e:
    print("Error: Some error in Calculation", e)
    '''
'''
try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    c= 9
    print(a+b)
    print(a/b)
    print(c+10)
except ZeroDivisionError as e:
    print('Zero Division Error : ',e)
except ValueError as e:
    print('Value Error : ', e)
except TypeError as e:
    print('Type error: ', e)
except NameError as e:       # c is not defined
    print('Name error: ', e)
except Exception as e:
    print('Some Error Occured', e)
'''  
try:
    length = int(input("Please enter length: "))
    breadth = int(input("Please enter breadth: "))
    area = length * breadth
    print("Area - ", area)
except TypeError as type_err:
    print("Error: - ", type_err)
else:
    perimeter = 2*(length * breadth)
    print("Perimeter: ", perimeter)
print("This is outside try block")

try:
    num = int(input("Please enter a Number: "))
    print("Number you entered: ", num)
except ValueError:
    print("Not a valid number")
else:
    cube = num**3
    print("Number: ", num, "And Cube: ", cube)
finally:
    print("This is always get executed")
