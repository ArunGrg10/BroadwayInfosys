# Closure is the concept in Python which fulfills the following:
# 1. There should be a nested function (a function inside another function)
# 2. An inner function must reference the argument from outer function
# 3. Outer function should return the inner function

def closure_fxn(messg):
    def inner_fxn():
        print(messg)
    return inner_fxn

result = closure_fxn("hello world")
result()

# The above function is the simplest closure that can be made in python, CLosure are basis of decorators in python,
