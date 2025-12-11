class Person:
    #constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    #getter method for age
    def get_age(self):
            return self.age
    # setter method for age    
    def set_age(self, age):
            self.age = age

    def get_gender(self):
            return self.gender
        
    def set_gender(self, gender):
            self.gender = gender
    
    def __str__(self):
          return f'{self.name}, {self.age}, {self.gender}'

print(__name__)
p = Person("Shweta", 32, 'f')
print(p)

person = Person('Amit', 25, 'f')
print(person.name, person.get_age())

person.set_age(29)
print(person.name, person.get_age())

person.set_gender('m')
print(person.name, person.get_age(), person.get_gender())


class Persons:
    def __init__(self, name):
        self.name = name

p = Persons("Shweta")
print(p)
