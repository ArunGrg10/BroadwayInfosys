# python lists are mutable data-types and are sequential (also an iterable)
# Lists are created enclosing data in big brackets "[]" or using built-in function list()

# Creating an empty list
a= p[]
b= list()

# creating non-empty list
a= [2, 4, 5]
vowels= ["a", "e", "i", "o", "u"]
# the above are the examples of list with homogenous data-types

# List can also contain heterogenous types
a= [1, 3, 2, ["a", "e"], ("o", 3), {2, 4, 5}, {"a": 1, "b", 2}]


##### Accessing List Items #####
# List items can be accessed using indexing and slicing

# Indexing in list starts form 0 for forward traverse and -1 for reverse traverse
vowels= ["a", "e", "i", "o", "u"]
print(vowels[0]) # a
print(vowels[2]) # i
print(vowels[4]) #u
print(vowels[-3]) # i

print(vowels[10]) # IndexError: list index out of range
print(vowels[-8]) # IndexError: list index out of range
## index must be integer not float and must be inside big bracket

# Item assignment is possible in list as it is mutable
vowels[1] = "E"
print(vowels)

# List Slicing
a = ["a", "e", "i", "o", "u", "f", "g", "h", "j"]
print(a[0:5]) # ["a", "e", "i", "o", "u"]
print(a[:5]) # same as above
print(a[2:]) # ["i", "o", "u", "f", "g", "h", "j"]

print(a[2:7]) # ["i", "o", "u", "f", "g"]
print(a[7:2]) #[]

print(a[o:-2]) # ["a", "e", "i", "o", "u", "f", "g"]
print(a[:-2]) # same as above
print(a[-7:-2]) # ["i", "o", "u", "f", "g"]
print(a[-2:-7]) # []
 print(a[2:-1]) # ["i", "o", "u", "f", "g", "h"]

# List Operations
# Concatenation
a = [1, 2, 3]
b = [4, 5, 6]
result = a+b
print(result) # [1, 2, 3, 4, 5, 6]

# Membership Operation
print(2 in [1, 2, 3]) # true
print(3 not in [1, 2, 3]) # false

