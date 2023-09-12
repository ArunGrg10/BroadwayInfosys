"""
# Create a decorator "login_required" which checks the password provided by the user. If the password matches
# "1234" then the user can access the function else show message "your password is invalid"
def login_req (func):
    def inner(*args):
        p = int(input("Enter the passcode : "))
        if p == 1234:
            print("the passcode is correct.")
            return func(*args)
        else:
            print("the entered pass is incorrect.")
    return inner

@login_req
def mess(a,b):
    return a + b

print(mess("thank", " you"))
"""

# Create a decorator which calculates the amount of time that it took to execute a function

import time
def execTime(func):
    def secs(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end  = time.time()
        print(f"execution time is {end-start} seconds.")
        return result
    return secs
@execTime
def clock(d,c=234):
    for i in range(100000000):
        continue
    return d+c

print(clock("thank you", c= " everyone"))
