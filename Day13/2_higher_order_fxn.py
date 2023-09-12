# A function that takes another function as an argument is called higher order function
# list ko sort() function ma use gareko thyo
# sorted(), map(), reduce(),ets. are the higher order funcitons in python

# map(function, iterable)
# map takes function as first parameter and iterable as a second parameter
# It maps every element of the iterable to some other form
# The lenth of initial iterable and final result is same in map

data= [1,2,3,4]
def cubed(elem):
    return elem ** 3
result = map(cubed,data)
print(result) # <map_object> which is an iterator and cab be looped. But tosee its element we need
# convert it to somoe other dataype

print(list(result)) # hamlai result ekai thauma ekai talli herna man xa bhane

# comprehension le list ma nachaida pani list ma result dinxa

for each in result: # yo iterate hudaina becz pailai iterate bhako feri iterate hudaina
    print(each)


# filter()
# it also takes function and iterable as arguments
# It picks certain elements from the initial iterable
# But the size of initial iterable and final result may not be same in case of final (either less or equal but not increase)

data = [1,2,3,4,5,6,7,8,9,10]
def get_even(elem):
    if elem % 2 == 0:  # or return elem % 2 == 0
        return True
    else:
        return False


result = filter(get_even,data)
print(result) # <filter object>
print(list(result)) # [2,4,6,8]

# reduce()
# It also takes function and iterable as arguments
# It does aperation based on the given function and return a single value

from functools import reduce

data = [1,2,3,4,5]
def add(x,y):
    return x+y

result = reduce(add,data)
print(result) # 15