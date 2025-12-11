# Type Conversion
# Explicit type conversion
x =int(4) # 4
y= int(7.5) # 7
z=int("89") # 89
print('x,y,z: ', x,y,z, type(x), type(y),type(z))

a =float(4) # 4.0
b= float(7.5) # 7.5
c=float("89") # 89.0
print('a,b,c: ', a,b,c, type(a), type(b),type(c))

aa= str('4') # 4.0
bb= str('7.5') # 7.5
cc=str("89") # 89.0
print('aa,bb,cc: ', aa,bb,cc, type(aa), type(bb),type(cc))

# type conversion str to list
hello_text ='Hello! How are you ?'
print('my text string is:', hello_text, type(hello_text))
hello_text_list= list(hello_text)
print('my text string after typecast to list is:', hello_text_list, type(hello_text_list))


# tuple/list type conversion to dictionary
pairs=[("name","Alice"),("age",25), ("city","NYC")]
print('Pairs tuple:', pairs, type(pairs))
person= dict(pairs)
print('pairs type conversion to person dictionary: ', person, type(person))

