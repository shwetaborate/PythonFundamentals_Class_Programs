x =10
x+= 5
x=x+5
print(x)

x = [1,2,3]
y = [1,2,3]
print('Check if x is y: ', x is y)
print('Check if x == y: ', x == y)






message = 'Hello There'
lang ={1: 'python', 2: 'Golang'} #dictionary

#The in operator checks if 'h' is a substring of message.
print('Is h present in message : ','h' in message)  # will be true since case sensistive

print ('Is 2 in lang : ', 2 in lang)

# if else - check indentation
if "Python" in lang.values():   # with values() method
    print("Value python exists.")
else:
    print("Value python does not exist.")

num = int(input('PLease give a numerical value: '))
if num > 0:
    print('Value is positive')
elif num< 0:
    print('Value is negative')
else:
    print('You have entered zero')

# nested if else
num2= 5
if num2 >= 0:
    if num == 0 :
        print('Number is 0')
    else:
        print('Number is positive')
else:
    print('Number is negative')

word = 'wisdom'
for i in word:
    print(i,end = "+ ")

marks = [50,90,80,40,90,60]
for elem in marks:
    print('Marks obtained: ',elem)

fruits =['apple', 'banana', 'orange', 'mangoes']
for fruit in fruits:
    print('List of fruits: ', fruit)

numbers = range(6)
print(numbers)
print(list(numbers))

for i in range(2,9,2):
    print('This is with start: ',i)