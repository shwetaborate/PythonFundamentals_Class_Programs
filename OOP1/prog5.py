# base class
#inheritance
class Company:
    def __init__(self, project, location):
        # protected variable
        self._project = project
        self.location = location

    def __str__(self):
        res = "Project Title: " + self._project + "\n"
        res += "Location of project: " + self.location
        return res


class Employee(Company):
    def __init__(self, name, project, location):
        super().__init__(project, location)
        self.name = name

    def display(self):
        res = "Employee Name: " + self.name + '\n'
        res += "Working on Project: " + self._project + '\n'
        res += "My location: " + self.location + '\n'
        return res


emp = Employee("Satish", "Software Development", "Mumbai")
print(emp.display())
