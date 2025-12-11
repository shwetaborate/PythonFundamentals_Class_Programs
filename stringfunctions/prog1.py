

s1= 'Hello '
s2= 'Hello'
s3= 'Hello'

print("Identity operator: ", s1 is s2)
print("Identity operator: ", s1 is not s2)

example = 'Hello Satish \"What\'s up\" '
print(example)

example2 = 'Went for a movie. It\'s awesome'
print(example2)

s1 = 'Hello We will be learning python'
s2 = 'We will be going out on saturday'
print('Length of s1: ', len(s1))
position = s1.index('We')
print("Give me index position: ", position)
print("s1 : ", s1)
changecase = s1.lower()

print('CHange the case of s1 to lower: ', changecase)
changeupper = s1.upper()

print('CHange the case of s1 to upper: ', changeupper)

print(changecase.islower())
print(changeupper.isupper())

s1 = 'Hello we will be learning python'
index = s1.find('movie')
print('Found the word with find', index)

message = 'python is programming language which is popular'
print('Number of occurance of p: ', message.count('p'))