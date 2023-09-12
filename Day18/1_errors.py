# There are broadly two types of errores in Python
# 1. Suntactic Error
# 2. Non-syntactic Error

# Syntactic errors occur when you mess up with the grammar of the Python
# Examples : Unwanted spaces, Indentation Error, Missed commas or colons etc


# All those errors except the syntax errors are non- syntactic errors
# They can further be classified as:
# 1. TypeError
# 2. ValueError
# 3. IndexError
# 4. KeyError
# 5. ZeroDivisionError
# 6. ModuleNotFoundError
# 7. AttributeError
# 8. NameError


# Examples
# print(2 + "hello") # TyoeError
# int("hello") # ValueError

# data = [1,2,3]
# print(data[10]) # IndexError

# student = {"name": "Harry", "age"30}
# print(student["address"]) # KeyError

#a = 2
#print(a / 0) # ZeroDivisionError

# import mat # ModuleNotFOundError

# a = [2,3,4]
# a.join(",") # AttributeError. join() is string method

# nums = [1,2,3]
# print(num) # NoneError
