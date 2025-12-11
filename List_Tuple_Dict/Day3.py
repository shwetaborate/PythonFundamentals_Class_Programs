#single assignment
nums= [1,2,3,4,5,6]
print(nums, type(nums))

# list - mutable - can be changed after definition
colors=['red','yellow','green', 5,6,7]
print('Print List: ',colors, type(colors))
print('Print element 4 of list: ',colors[4])
''' allows assignment of items post declaration'''
colors[3]= 'banana'
print('Print element 3 of list: ', colors[3])
print('Print List: ',colors, type(colors))

# tuple - immutable - cannot be changed after definition

colors2=('red','yellow','green', 5,6,7)
print(colors2, type(colors2))
print('Print element 4 of list: ',colors2[4])

'''
colors2[3]= 'banana'
print('Print element 3 of list: ', colors2[3])
print('Print List: ',colors2, type(colors2))

get the following error - cannot assign

'''
# Dictionary - key value pairs - mutable

languages={1:'java',2:'go',3:'typescript'}
print('Languages: ', languages, type(languages))

# set - mutable - unique elements

student_id={111,112,113,114,115,114,116}
print('Student id set: ', student_id, type(student_id))

student_mix={111,112,113,114,115,114,116,'one', 'two'}
print('Student id mix set: ', student_mix, type(student_mix))

# frozenset - programmitically make list immutable
#used when we need to make set, list or dictionary, etc immutable temporirly
#can aslo use set(have use for loop and iterator) or dictionary not tuple(as its already immutable)
my_list=[1,2,3,4,5] 
frozen_set= frozenset(my_list)
print('Frozen set: ', frozen_set)
my_list[2] ='changefrozen' # trying to change element
print('Frozen set: ', frozen_set)


