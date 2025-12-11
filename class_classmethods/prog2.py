#class methods
class Btech_Student:
    uni = 'Savitribai Phule University' # class variable
    year = 'First_year'
    fullname = None
    gender = None

    #public instance methods
    def __init__(self, name, gender):
        self.fullname = name
        self.gender = gender

    @classmethod
    def change_year(cls, year):
        #class_name.class_variable
        cls.year =year

    @classmethod
    def transfer_uni(cls, uni):
        cls.uni = uni
    
    #instance method
    def get_details(self):
        res = 'Name: %s\n'%(self.fullname)
        res += 'Gender: %s\n'%(self.gender)
        res += 'Year: %s\n'%(self.year)
        res += 'University: %s\n'%(self.uni)
        return res
    
student = Btech_Student('Harry', 'M')
print(student.get_details())
student.change_year(2026)
print(student.get_details())
#print(f'FullName: {student.fullname}, Gender: {student.gender}, University: {student.uni}, Year: {student.year}')

student2 = Btech_Student(input('Name: '),input('Gender: ') )
#student2.name = input('Name: ')
#student2.gender = input('Gender: ')
print(student2.get_details())



