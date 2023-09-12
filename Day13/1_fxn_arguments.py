## Order of the function arguments is important to note.
# Arguments are the values passed during function call and parameters are the values taken in function definition

# Order of the arguments
# 1. Positional / Compulsory arguments
# 2. Default arguments
# 3. Arbitrary arguments

def addition(a,b,c=23):  # here a and b are positional arguments and c is default argument
    return a+b+c

print(addition(3,4,6)) # here c is a keyword argument

# if we send value in the function call then the default value always gets override
# here c=5 override c=10





















# Arbitrary Arguments
# Arbitrary arguments can take random number of elements in the function call. They are like an
#expandible bucket

def addition(*args):
    print(args)
    print(type(args))
    return sum(args)

print(addition(1,2))
print(addition(1,2,3))
print(addition(1,2,3,4,5))


def addition(**kwargs):
    print(kwargs)
    print(type(kwargs))
    return sum(kwargs.values())


print(addition(a=1, b=2, c=3)) # 6
print(addition(a=1, b=2, c=3,d=4, e=5)) # 15

# arbitrary arguments also have their own order. * args should always come before than **kwargs

def addition(a , b , c , d=1 ,e=2,f=3,*args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(args)
    print(kwargs)
    #return sum(args)
    return sum(kwargs.values())

print(addition(4,5,6,7,8,9,10,11,12,13,p=14,q=16)) # args le 10,11,12,13 args le linxa ani jati thape ni args le linxa
                                                    # p ra q chai kwargs le lilnxa
