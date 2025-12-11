#Dictionary
d1 = {}
d2 = dict()
nums = {1:"one", 2:"Two", 3:"Three", 4:"Four", 5:"Five"}

print(nums)
print(type(nums))
cities = {"India":"Delhi", "Italy":"Rome", "England":"London"}
print(cities)
print(type(cities))

for key in cities:
        print(key, end = "\t")
print("\n")

for i in cities.values():
        print(i, end="\t")
print("\n")

for key,value in cities.items():
        print(f"{key} : {value}")

cities = {"India":"Delhi", "Italy":"Rome", "England":"London"}
cities["Spain"] = "Madrid"
cities["India"] = "New Delhi"

itemRemoved = cities.pop("Italy")

print(itemRemoved)
print(cities)
itemRemoved2 = cities.popitem()
print(itemRemoved2)
cities.clear()
print(cities)

#nested Dictionary
student = {
        "Amit" : {"Age": 26, "Grade": "a"},
        "Sachin" : {"Age": 21, "Grade": "b"},
}

print(student["Sachin"]["Age"])