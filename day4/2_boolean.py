# True and False are the boolean data-typed in Python. Keywords "True" and "False" are used to
#represent true state annd false state rersp.

#### Operations that give boolean type ####
# 1. Comparison Operation
a= 5
b= 3
print(a > b) #True
print(a == b) # False
print(a<b) # False
print(a >= n) #True
print(a<=b) # False
print(a!=b) # True

# Logical operation
a = 5
b= 3
print(a > b and a != b) # True
print(a != b or a > b) # True
print(not True) # False
print(not False) # True
 print(not a) # False

# Membership Operation
print("a" in ["a", "e", "i"]) # True
print("i" not in ["a", "e", "i"]) # false

# Identity operation
a = 1
b= 1
print(a is b) # Trye
print(id(a)) # True
print(a is not b) # False
print(id(a) != id(b)) # False

### concept of Truthy and Falsy ###
a = 5
print(not a) # False

# any non-zero or non-empty data-type including True itself is a truthy
# data type
# 5, 1, -23, [1,2], (4,5), {-4,-5,"a"}, {"a":1}, True; all these data are the truthy data types

# In contrast, all empty data-types, zero and None including False are falsy datatypes
# 0, [], {},set(), '', None, False; all these are Falsey data types/

# How can we verity datat is turthy or falsy
# we can use bool() built in function

# check for truthy
a = 4
b = -3
c = [2, 3,4]
d= (2, 4)
e= {"a": 1}
f= {1,3}
g= "hello world"
h= True

print(bool(a)) #True
print(bool(b)) #True
print(bool(c)) #True
print(bool(d)) #True
print(bool(e)) #True
print(bool(f)) #True
print(bool(g)) #True
print(bool(h)) #True

# applying not operation to any truthy value results in False
Print(not a) # False

# check for falsy
a= 0
b= []
c= ()
d= {}
e= set()
f= ''
g= None
h= False
print(bool(a)) #False
print(bool(b)) #False
print(bool(c)) #False
print(bool(d)) #False
print(bool(e)) #False
print(bool(f)) #False
print(bool(g)) #False
print(bool(h)) #False
print(bool()) # False

# aApplying not operation to any falsy value results i True
print(not a) # True
print(not None) # True

#### Python Boolean ia a Sub-class of Integer. ####
# True is integer 1 and False is integer 0

print(True + 1) # 2
print(34 + False) # 34
print(342 * False) # 0
print(True + True) # 2
print(True + False) # 1