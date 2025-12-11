
#without list comprehension

fruits = ['apple', 'mango','pineapple', 'kiwi', 'cherry' ]
fruits2 =[]
for f in fruits:
    if 'a' in f:
        fruits2.append(f)
print(fruits2)

# with list comphrehension

fruits = ['apple', 'mango','pineapple', 'kiwi', 'cherry' ]
fruits2 = [f for f in fruits if 'p' in f]
print(fruits2)

numbers = [1,2,3,4]
newNum = [num * 2 for num in numbers]
print(newNum)

words = ['javascript', 'python', 'java']
upper_case = [word.upper() for word in words]
print(upper_case)

#without list comprehension - find odd numbers

nlist = [[1,2,3], [4,5,6], [7,8,9]]
nlist2 = []

for n in nlist:
    for n2 in n:
        if n2 % 2 != 0:
            nlist2.append(n2)

print(nlist2)


mlist = [[1,2,3], [4,5,6], [7,8,9]]
mlist2 = [n2 for n in mlist for n2 in n if n2 % 2 != 0]
print("With list comprehension: ",mlist2)

# higher order function
# use map(), lazy iterator. have to convert to list frist then print
import math
num2 = [5,9,23,32,12]
def square_root(n):
    #return n * n
    return math.sqrt(n)

num3 = map(square_root, num2)
num4 = map(lambda n: n ** 0.5, num2)

print(f" Sq root for : {list(num3)}")
print(f" with lambda function: {list(num4)}")