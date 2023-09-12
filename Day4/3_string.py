# Strings are the immutable datatypes in python
# They are sequential datatypes (iterables)

#creating an empty string
a= ""
b= ''
c= """ # docstring/ triple-quoted string
"""
c= ''' # docstring/ triple-quoted string
'''
e= str() # str() is built-in function

# Quote characters
message = "I'm learning python" # double quote outside and single quote inside
message = 'I'm learning python' # this raises error

message = 'He said, "Python is awesome!"' # single quote ouside and double quote insie
# message = "He said, "Python is awesome!" # this raises error

# But we have the feature of escape sequece in python if we want to use sile quote both inside
# and outside

message = 'I\'m learning python' # here \' is an escape sequence
message = "He said, \"Python is awesome\"" # here \" is an escape line

#Escape sequence suppresses the usual meaning of character and gives new meaning
# \', \", \n, \t etc are escape sequences

print("hello\nworld")# hello <new line> world
print("hello\tworld") # hello <tab> world

#### Triple quoted string ###

# Triple quoted strings can be used as docstring.


def addition(a,b):
    """
    this is a funcion to add two integers
    :param a:
    :param b:
    :return:
    """
    return a + b
print(help(addition))

message= "hello world"
message[2] = "l" # it raises error because we can't change the existing item in string as it is immutable
# del nessage[2] # yo ni mildaina
del message # it deletes the string

# Iteration through string
message= "Hello World"
for each in message:
    print(each) # "H", "e", "l", "l", "o", "", "w", "o", "r", "l", "d"

message= "Hello World"
for each in message[:5]:
    print(each) # "H". "e", "l", "l", "o"



