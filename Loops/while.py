# while loop
count = 1
while count <=5:
    print("Count: ",count)
    count +=1


number= int(input("Tell us number to print table: "))
i=1
while i<=10:
    result = number * i
    print(f'{number} x {i} = {result}')
    i+= 1

records = [10,20,30,40,50,60,70,80,90,100]
for i in records:
        if i==60:
             break
        print("Values in the loop: ", i)
print('\n')
print('Out of the loop')

# while continue

number = 20

while number > 0:
    number -= 1
    if number == 8:
        break
    print(number)
print("Loop Over")


for num in range(10):
    if num == 7:
        break
    print(num)


for num in range(10):
    if num == 5:
        continue
    print("for continue", num)


number = 20
while number > 0:
    number -= 1
    if number == 8:
        continue
    print('For continue while loop', number)
print('Loop over')