#positional arguments
def example_posArgs(num1, num2, num3):
     sum = num1 + num2 + num3
     avg = sum / 3
     s1 = f"Numbers we gave {num1}, {num2} and {num3} and sum is: {sum}"
     s1 = s1 + "\nAverage is {:.2f}".format(avg)
     return s1

print(example_posArgs(11,20,13))


#default arguments
def example_defArgs(num1, num2=1, num3=2):
     sum = num1 + num2 + num3
     return f"Numbers are {num1}, {num2} and {num3} and sum is: {sum}"

print("this for default arguments 1:", example_defArgs(1))
print("this for default arguments 2:", example_defArgs(1,4))
print("this for default arguments 3:", example_defArgs(1,4,9))

#keyword arguements

def example_keyrdArgs(num1,num2,num3):
    sum = num1+num2+num3
    avg = sum/3
    s1= f"Numbers are {num1}, {num2} and {num3} and sum is : {sum} "
    s1 = s1+ "\n Average is {:.2f}".format(avg)
    return s1

print("Keyword Arguments : ", example_keyrdArgs(num1 =3, num2 = 5, num3= 6))

# arbitary arguments

def find_sum(*x) :
    result = 0
    for num in x:
            result = num + result
    print("Sum : ", result)


find_sum(2)
find_sum(1,2,3,4,5,6,8)

def find_avg(*x) :
     results = 0
     i=0
     for num in x:
          results = num + results
          i = i+ 1
     avg = results / i
     return avg

average = find_avg(3,3,3,4,5,6,7)
print(" Avg is : {:.2f} ".format(average))

print (f" Average2 : {find_avg(2,1):.2f}" )

#keyworded arguments

def get_dictInfo(**info):
     print('Data Type of argument : ', type(info))
     for key, value in info.items():
          print("key: ", key, "Value:", value)

get_dictInfo(fname = 'Amit', lname = 'abc', age = 24, mobileNumber = 1234566789)

#nested fucntions

def greeting(fname,lname): # outer fn with two arguments
     def fullName(): # inner fn\
          return fname + " " + lname
     print("Hi "+ fullName())

greeting ('Amit', 'Sawant')     


#local scope variables
def myfunction01(a,b):
     x = 10 #x is local variable
     result = x+a+b #result is local variable
     return result
print("Result is:", myfunction01(2,4))


#accessing outer variables
def myOuterFunction():
     outer_var = "\nI am in outer function"
     def myInnerFunction():
          print("I am accessing outer function variable", outer_var)
     myInnerFunction()

myOuterFunction()