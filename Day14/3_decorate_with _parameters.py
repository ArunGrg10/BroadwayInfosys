def decorat_me(func):
    def inner_func(txt):
        print("I'm the extra functionality !!")
        return func(txt)
    return inner_func

@decorat_me
def message(txt):
    return txt


#message = decorate_me(message)
print(message("hello"))

##
def decorate(func):
    def inner_fxn(*args):
        print("hello")
        return func(*args)
    return inner_fxn

@decorate
def message(a,b):
    return a+b

print(message(2,3))


##

def decorate(func):
    def inner_fxn(*args, **kwargs):
        print("hello")
        return func(*args,**kwargs)
    return inner_fxn

@decorate
def message(a,b,c= "Thanks"):
    return a+b,c

print(message(1,2, c= " Thanks"))