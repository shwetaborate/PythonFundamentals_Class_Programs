#strings
for letter in 'completed':
    if letter == 'm':
        break
    print(letter)

for letter in 'completed':
    if letter == 'e':
        pass
    print(letter)


# string slicing

b = "Hello, World!"
print(b[2:5])
print(b[-10:-3])
print(b[2:-3])
print(b[4:])
print(b[:4])


s1 = 'Hello World'
s2 = 'Good Evening'
s3 = "Hello World"

print(s1 == s3)

if s1 > s2:
    print('String s1 is greater than s2')
else:
    print('string s2 is greater than s1')