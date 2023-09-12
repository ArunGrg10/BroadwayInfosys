# functions are the blocks of reusable codes.
# THey are defined as a place and can be called from multiple different locations
# def is the keyword to create a function in python

def message(): # This is defining a function
    return "hello world" # This is return of the function


# return in the function is no tmandatory. If you do not return anything then
# it returns None by default

result = message() # This is the function call
print(result) # hello world

# There are several types of arguments and parameters in python functions. They are
# categorized as:
# 1. Positional Argument
# 2. Default Argument
# 3. Arbitrary argument