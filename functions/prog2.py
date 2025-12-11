#this is function defination without arguments
def message():
        print("This is my first function. With no arguments / parameters")

#this is function call
message()

print("First Value:")
num1 = int(input())
print("Second Value:")
num2 = int(input())

#this is function defination with arguments
def addition(firstNo, secondNo):
        return firstNo + secondNo

#this is function call
result = addition(num1, num2)
print("This is the output: ", result)
#alternative method
print("This is the output (method 2)", addition(num1, num2))

f1= input('Tell us yr first name')
l1= input('Tell us yr  last name')

def printFullname(fname, lname):
        wm ='Welcome'
        print(f'{wm} {fname} {lname}')


printFullname(f1,l1)

def multiOperations(a,b,c,) :
        sum = a+b+c
        multi= a*b*c
        additionofsquare =(a*a) + (b*b) + (c*c)
        return sum, multi, additionofsquare

n1, n2, n3 = 5,2,3
add, multiplication,addnsquare= multiOperations(n1, n2, n3)
print('Numbers are: ', n1, n2, n3)
print('Addition: ', add)
print('Multiplication: ', multiplication)
print('Addition of square of each number: ', addnsquare)