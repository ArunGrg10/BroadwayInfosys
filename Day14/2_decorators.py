# Decorators are the function that add extra functionality to the existing function

def decorate_me(func):
    def inner_func():
        print("I'm the extra functionality !!")
        return func()
    return inner_func

@decorate_me
def message():
    print("hello world")

#message = decorate_me(message)
message()

