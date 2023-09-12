# Create a function that takes a text message and simply return the text message
# Create a dicorator which changes the text message into the upper case text.

def to_upper_case(func):
    def inner_func(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return inner_func

@to_upper_case
def message(txt):
    return txt

print(message("hello world"))

#
def to_upper_case(func):
    def inner_func(*args, **kwargs):
        result= func(*args, **kwargs)
        if type(result) != str:
            return result
        return func(*args, **kwargs).upper()
    return inner_func

@to_upper_case
def message(txt):
    return txt

print(message(234))

# Create a decorator "login_required" which checks the password provided by the user. If the password matches
# "1234" then the user can access the function else show message "your password is invalid"

def login_required(func):
    def inner_fxn(*args, **kwargs):
        result = int(input("input the password"))
        if result == 1234:
            print("you can have access to the application")
            return func(*args, **kwargs)
        else:
            return "invalid password"
    return inner_fxn

@login_required
def password(txt,b):
    return txt
print(password(2,b=3))


# task 3
# print(time.time())
# Create a decorator which calculates the amount of time that it took to execute a function

import time

def execTime(func):
    def inner_fxn(*arg, **kwargs):
        start = time.time()
        result = func(*arg, **kwargs)
        end = time.time()
        print(f"execution time is {end - start} seconds")
        return result
    return inner_fxn

@execTime
def message(txt):
    return txt

print(message("Hello I am Arun"))


