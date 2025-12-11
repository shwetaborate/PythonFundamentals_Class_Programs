#string functions
txt = "Compan22yX"

x = txt.isalpha()

print(x)

txt = "Compan22yX"

x = txt.isalpha()

print(x)

sampletext2 = "we will be going out in december"
print("this is title:", sampletext2.title())
print("this is capitalize:", sampletext2.capitalize())

# tuples

demoTuple1 = (1, 2, 3, 4, 5, "Amit", "Vishal", 2.5, 3, 7)

demoTuple2 = 1, 2, 3, 4, 5, "Amit", "Vishal", 2.5, 3, 7

demoConstructor = tuple((1, 2, 3, 4, 5, "Amit", "Vishal", 2.5, 3, 7))

students_name = ("Amit", "Satish", "Rakesh", "Umesh")
print(demoTuple1)
print(demoTuple2)
print(demoConstructor)
print(students_name)

single_element = (1,)
empty_element = ()
nested = (1,2,(3,4),'Satish','Manish')
nested2 = (1,2,(3,4),('Satish','Manish'))
print('Data Type single element: ',single_element,type(single_element) )
print('Data Type: empty element ',type(single_element) )
print('Nested Tuple: ', type(nested))
#print('nested tuple: ', nested[4])
print('nested2 tuple: ', nested2[2])
print('nested2 tuple: ', nested2[3][0])

a = 1,2,3,4,5,6,7,8
print('Is a tuple ? ', type(a))

print(a)
print(a[::])
print(a[6::])
print(a[:])
print(a[::-1])
b = a[2:]
print(b)
print(a[2:6:2]) # start, stop, step