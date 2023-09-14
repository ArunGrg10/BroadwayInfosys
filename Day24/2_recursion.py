# If a function is called from the defination of the same function then it is called as a recursive function


c= 0
def count():
    global c  # esma c ko value baira bata halnu parxa
    print(c)
    c += 1
    if c == 10:
        return
    c += 1
    count()

count()

# WAP to calculate the factorial of 5 in three ways:
# normal loop
# reduce() function
# recursion
# 5*4*3*2*1

# 1. normal loop
a= 1
for i in range(1,6):
    a = a*i

print(a)

# 2. reduced
from functools import reduce

result= reduce(lambda x,y: x + y, range(1,6))
print(result)

# 3. recursion

def factorial(num):
    if num == 0:
        return 1
    return num = factorial(num-1)

result = factorial(5)
print(result)

# 5 * factorial(4)
# 4 * factorial(3)
# 3 * factorial(2)
# 2 * factorial(1) # 2 * 1 = 2
# 1 * factorial(0) # 1 * 1 = 1 since if condition
