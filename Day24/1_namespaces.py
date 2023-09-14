# Namespaces determince thew scope of the variales and objects inpython
# Namespace is explained by LEGB rule. (loacl, enclosed, global , built-in)
# There are 4 types of namespaces
# 1. Local Scope
# 2. Enclosed Scope
# 3. Global Scope
# 4. Built-in Scope

# Built-in Scope
# If the scope of package or object is all over the project then it is an object of built-in scope
# Example: Ptython built-in libraries like math, os, json etc.
# import math   # Built-in Scope


# Global Scope
# If the scope of the variable or object is limited to one python module then it has a global scope
# to that module.

a = 2 # this variable 'a' is limited to this python  file only

# Local Scope
# If the variable scope is limited function then it has local scope

a= 12 # global scope
def tst_func():
    a = 20   # local scope
    print(a)
print(a) # 12
tst_func() # 20
print(a) # 12

# Enclosed Scope
# If the scope of the variable or object is liited to a nested function then it has an enclose scope

a = 12 # global
def outer_fxn():
    a= 20 # local
    def inner_fxn():
        a = 30 # enclosed
        print(a) # 30
    inner_fxn()
    print(a) # 20

print(a) # 12
outer_fxn()
print(a) # 12

# But, we have a "global" keyword which can define even a local variable as global

a = 20
def outer_function():
    global a
    a = 40
    def inner_function():
        a = 30
        print(a) # 30
    inner_function()
    print(a) # 40

print(a) # 20
outer_function()
print(a) # 40


# non-local
a = 20
def outer_function():

    a = 40
    def inner_function():
        nonlocal a
        a = 30
        print(a) # 30
    inner_function()
    print(a) # 30

print(a) # 20
outer_function() # 30
print(a) # 20
