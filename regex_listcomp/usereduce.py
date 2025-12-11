
from functools import reduce

# Convert the iterator to a list
data = [1, 2, 0, None, 5]
filtered_list_iterator = filter(None, data)
filtered_list = list(filtered_list_iterator)
print(filtered_list)

dataList = ["apple", "", None, "cherry", 0, None]
improvedList = filter(None, dataList)
normalList = list(improvedList)
print(normalList)

students = [
    {"name": "Ashish", "id": 3},
    {"name": "Ramesh", "id": 5},
    {"name": "Santosh", "id": 10},
    {"name": "Amit", "id": 12}
]

newStudents = list(filter(lambda n: (n['id'] > 5), students))
print(newStudents)

#from functools import reduce - pls import
def find_minimum(n1, n2):
    return n1 if n1 < n2 else n2

numbers2 = [5, 9, 23, 32, 2, 12]

result = reduce(find_minimum, numbers2)
print(result)
