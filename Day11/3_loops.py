# loops are used to execute certain blocks of code repeatedly
# they are usede to reduce manual efforts in the algorithms

# for loops in python with different datatypes
vowels = ["a", "e", "i", "o", "u"]

for each in vowels:
    print(each)
else:
    print("this is executed if the main loop is completely ")

# looping is similar to list in tuple and set
# let's see how is it done in dictionary

student = {"name": "Jane", "age": 34, "address": "KTM"}

# looping in dictionary keys
print(student.keys()) # dict_keys(["name", "age", "address"])

for key in student.keys():
    print(keys)

# Looping in dictionary values
print(student.values()) # ["Jane", 34, "KTM:]
for value in student.values():
    print(value)

# Looping through both dictionary keys and values
print(student.items()) # [("name", "Jame"), ("age", 34), ("address", "KTM")]

for key, value in student.items():
    print(key)
    print(value)
