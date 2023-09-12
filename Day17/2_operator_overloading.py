# Each operator in Python has it's own method which is called when the operation is \
# carried out

# Magic methods in python iare the special methods created by using dpouble underscore.
# __add__(), __mul__(), __sub()__, __gt__() etc, are some examples of magic methods

a = 1
b = 2
result = a+b
print(result)

result = a.__add__(b)
print(result) # 3

# So, everytime an operation is carried out, a magic method is called
# Magic mehtods are also called as dunder methods
