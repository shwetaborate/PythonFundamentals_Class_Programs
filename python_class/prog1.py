#class
class Box:
    length = None
    breadth = None
    def set_dimension(self, length, breadth):
        self.length = length
        self.breadth = breadth
        return f'Length : {self.length} and Breadth: {self.breadth}'
    def calculateArea(self):
        area = self.breadth * self.length
        return 'Area {:.2f}'.format(area)

bxObj = Box()   # creatin gobject
a = float(input('Enter length: '))
b = float(input('Enter breadth: '))
bxObj.set_dimension(a,b)

print(bxObj.calculateArea())

print('Get attribute length: ', getattr(bxObj, 'length'))
print('Get attribute breadth: ', getattr(bxObj, 'breadth'))

class student:
    # private variables and methods are defined with double underscore
    # private variables
    __name = None
    __rollno = None
    __branch = None

    def set_details(self, name, rollno, branch):
        self.__name = name
        self.__rollno = rollno
        self.__branch = branch

    # private method
    def __displayDetails(self):
        return f"Roll No = {self.__rollno} \t Name = {self.__name} \t Branch = {self.__branch}"

    # to call private method you have to make a public method
    def callPrivateDetails(self):
        return self.__displayDetails()
    

studentObj = student()
studentObj.set_details('Satish', 215,'Bsc Comp Science')

print(studentObj.callPrivateDetails())

# mangled naming - not a good practice

