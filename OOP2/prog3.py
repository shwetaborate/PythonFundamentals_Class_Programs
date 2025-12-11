# operator overloading

class Bankaccount:
    def __init__(self, balance):
        self.balance =balance
    
    def calculateInterest(self):
        rate = 0.02
        interest = self.balance * rate
        print(f"Base interest calculated: {interest: .2f}")
        return interest
    
class savingsaccount(Bankaccount):
    def calculateInterest(self):
        rate = 0.05
        interest = self.balance * rate
        print(f"Savings account interest calculated: {interest: .2f}")
        return interest
    
bankobj = Bankaccount(10000)
print(bankobj.calculateInterest())
    
savacc = savingsaccount(100000)
print(savacc.calculateInterest())

'''
acc3 = savacc + bankobj
print(acc3.balance)
'''

# operator overloading
class Book:
    def __init__(self, pages):
        self.pages = pages
    
    def __add__(self,other):
        return self.pages + other.pages

b1 = Book(400)
b2 = Book(300)

print("Total number of pages: ", b1 + b2)