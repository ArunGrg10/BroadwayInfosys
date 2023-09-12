# lamda are the elegant way of creating one-lner function
# lamda function do not have name. So, they are also called anonymous function

def squared(num):
    return num ** 2

print(squared(2)) # 4

lambda num: num ** 2

squared = lambda num: num ** 2 #
print(squared(4)) # 16

# map()
data = [1,2,3,4]
result = map(lambda elem: elem ** 3, data)
filter = filter(lambda elem: elem ** 3, data) # [1,
print(result)

# filter()
data= [1,2,3,4,5,6,7,8,9,10]
result= filter(lambda x: x % 2 == 0,data)
result = map(lambda x: x % 2 == 0,data)  #[False, true, false, true, false,true, false, true, false, true]
print(list(result))

#reduce()
from functools import reduce
data = [1,2,3,4,5]
result= reduce(lambda x, y : x + y,data)
print(result) # 15

# we can give numbers of parameter in lambda

