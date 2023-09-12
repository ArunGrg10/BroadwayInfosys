### Operators ###
#OPerators are the symbols in python o tin any programming language that carrry out
# arithmetilc and logical operations
#the python operators are
# 1. Arithmetic operators
# 2. Relational operators
# 3. logical operators
# 4. membership operators
# 5. identity operators
# 6. assignment operators

### Arithmetic operators ###
# 1. addition (+)
a =1
b =2
print(a+b)
# here a and b are operands whereas + is operator

print(a-b)

# modulus: modulus operators gives remainder of the divisio operation
x= 4
y= 2
print(x % y) #result
# exponential



# floor division (//)
# this operator omits the decimal values from the divilsion operation and gives floor value
print(3 // 2) #1
print(-3 //2) #

## Relational or comparison opertators ####
# =, <, >, != are the relational operators
# relational operators give boolean result (trui or false)
 a= 2
 b= 4
 print(a == b) # false
 print(a>b) # ture
 print(a>b) #false

 #### logical operators ###
 # and, or, not are the logical operators
 print(a > b or b != a)
 print(a > b ad a != b)
 print(not true) # false
 print(not false) #rue
 a =5
 print(not a) # false
 a = 0
 print(not a) # true.  Here it is using the concept of truthy and alsy which we will learn later

## assignment operators##
# is equal ot (=) is the siplest assighment operator
a = 2 + 3
# in above, 2 nd 3 are added and assigned to variable 'a'
# operator

a = 1
a = a + 1 #2
a += 1 #3
# += is also an assignmetn operators. others include +=, %=

### membership operaors ###
# in and not in are the membership operaots. we can use membership operator in sequence datatypes
print(2 in [1, 2, 3]) #true
print(3 not in [34, 3, 343, 34]) # false

## identity operator ##
# "is" and "is not" are the identity operators
a= [1, 2, 3]
b= a
print(a is b) # true
# here  a and b ar ehte smae obhect and lies at same memory location
print(id(a)) #true

b = a.copy()
print(a is b) # false
print(id(a) == id(b)) # false
# here a and b have same value but are in different memoty location

## precedence and associativity ##
# if an operation has multiple operators then precedence defines the order of such operators.
# if multiple operators have same precedence then the operation is done based on associativity
# normally all the operators have left-right associativity except "**"
print(2 * 3 / 3) #2. here multiplication and division have same precedence byt the associativity is rom left-right.
                 # so multiplication is done first and the division
 print(2 ** 3 ** 2)
 # for ** associativiy is from right-left. so, 3**2 is executed first and then 2**9
