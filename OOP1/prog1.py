#inheritance
# multilevel and multiple
#multilevel inheritance example

#grandparent class
class GrandParent:
    def __init__(self,grandparent_name):
        self.grandparent_name = grandparent_name
    def greet_grandparent(self):
        return f"Hello {self.grandparent_name}, the Grand Parent"
    
#Parent Class
class Parent(GrandParent):
    def __init__(self, grandparent_name, parent_name):
        super().__init__(grandparent_name)
        self.parent_name = parent_name
    def greet_parent(self):
        return f"Hello {self.parent_name}, the Parent"

#child class
class child(Parent):
    def __init__(self, grandparent_name, parent_name, child_name):
        super().__init__(grandparent_name, parent_name)
        self.child_name = child_name
    def greet_child(self):
        return f"Hello {self.child_name}, the Child"
    def getFullName(self):
        return f"Hello my Grandparent's name: {self.grandparent_name}\n and my Parent's name is : {self.parent_name}\n and my name is : {self.child_name}"  

c = child('Baba', 'Papa', 'Rano')
print(c.greet_parent())
print(c.greet_grandparent())
print(c.getFullName())

# Multiple Inheritance
class Department:
    def __init__(self, deptCode, deptname):
        # protected Variables
        self._deptCode = deptCode
        self._deptname = deptname

    def get_deptDetails(self):
        res = f"Dept Code: {self._deptCode}\n"
        res += f"Dept Name: {self._deptname}\n"
        return res


class Project:
    def __init__(self, project_name, client_name, project_manager):
        self._project_name = project_name
        self._client_name = client_name
        self._project_manager = project_manager

    def get_projectDetails(self):
        res = f"Project Name: {self._project_name}\n"
        res += f"Client Name: {self._client_name}\n"
        res += f"Project Manager: {self._project_manager}"
        return res

class Employee(Department, Project):
    def __init__(self, name, desig, project_name, client_name, project_manager,
                 deptCode, deptname):

        # Initialize Department
        Department.__init__(self, deptCode, deptname)

        # Initialize Project
        Project.__init__(self, project_name, client_name, project_manager)

        # Employee class instance members / variables
        self.name = name
        self.desig = desig


    def get_employeeDetails(self):
        dept_details = self.get_deptDetails()
        project_details = self.get_projectDetails()

        return (
            f"Employee Name: {self.name}, "
            f"Employee Designation: {self.desig}\n"
            + dept_details
            + project_details
        )


employeeObj = Employee(
    "Amit", "Software Developer", "Banking Application",
    "Abc bank", "Satish", "sde001", "IT"
)

print(employeeObj.get_employeeDetails())


# Hierarchical Inheritance
class Car:
    def car_wheel(self):
        print("The car has 4 wheels")


class BMW(Car):
    def model_info(self):
        print("This is for BMW")


class Audi(Car):
    def model_info(self):
        print("This is for Audi")


class Mercedez(Car):
    def model_info(self):
        print("This is for Mercedez")


bmwObj = BMW()
bmwObj.model_info()
bmwObj.car_wheel()

mercedezObj = Mercedez()
mercedezObj.model_info()
mercedezObj.car_wheel()