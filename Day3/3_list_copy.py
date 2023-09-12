# copy
a= [1, 2, 3]
b= a
print(a)# [1, 2, 3]
print(b)# [1, 2, 3]
print(a is b) # True

b= a.copy()
print(a)
print(b)
print(a is b) # False

# shallow copy
a= [[1, 2, 3], 4, 5]
b= a.copy()
a[0][1] = 7
print(a) # [[1, 7, 3], 4, 5]
print(b) # [[1, 7, 3], 4, 5]

# even if 'b' is copy of 'a', if we change any mutable object inside 'a' then the
# the change is also reflected in 'b'. This type of copy is called shallow copy.

### Deepcopy
from copy import deepcopy
a= [[1, 2, 3], 4, 5]
b= deepcopy(a)
print(a) # [[1, 2, 3], 4, 5]
print(b) # [[1, 2, 3], 4, 5]

a[0][1] = 7
print(a) #
print(b) #