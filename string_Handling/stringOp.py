#string
a, b, c = 1, 2, 3
print(a, b, c)

print("hi there", end= " ** ")
print("How are you")

day = 7
month = 11
year = 2025
print(day, month, year, sep="-")
print(day, month, year, sep="/")

name1 = "Ashish"
prof = "Developer"
print(name1 + " " + prof)

num1 = 22
num2 = 3
result = num1 + num2
print("sum of " + str(num1) + " " + str(num2) + " is: " + str(result))

# print results - can use %d, %s, %f as placeholders for diff data types (like C) for printing
n1=22
n2=3
results= n1 + n2
#printResult = 'Addition of %d and %d is %d'%(n1,n2,results)
#print(printResult)
print('Addition of %d and %d is %d'%(n1,n2,results))

name = 'Amit'
experience = 9
prof = 'software developer'
stringResult = '%s has %d years of expereince and he is %s by profession'%(name,experience,prof)
print(stringResult)


name1 = 'rakesh'
age= 22
gender = 'male'
print('Name of student: ',name, 'gender: ', gender, 'age: ',age)

# posiitonal formatting {} are placeholders
name2= 'Amit'
exp = 8
print('Name :{}, Exp:{}'.format(name2,exp))

# posiitonal formatting {} are placeholders - uses index for arguements - useful when you to resuse values
print('Name :{0}, Exp:{1}'.format(name2,exp))

# keyword-based formatting, where you name each placeholder and pass matching keyword arguments to .format().
print('name:{student_name}, Roll no:{rollno}'.format(student_name ='Amit', rollno= '23'))

# f-strings
len= 5
br =9
print(f'Length: {len}, Breadth: {br} then Area is {len*br}')

# float decimal points
print('Divsion of 22 by 7 is : %f'%(22/7))
print('Divsion of 22 by 7 is : %.2f'%(22/7))

# placeholder, format and modifier 
print('Divsion of 22 by 7 - placeholder and format is :{:.2f}'.format(22/7))

#fstring and modifier
print(f'Divsion of 22 by 7 - fstring is : {22/7:.3f}')

# 