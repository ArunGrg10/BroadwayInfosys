# Concatenation => We ca cocatenate strings using "+" operator

n1= "hello"
n2= "world"
print(n1 + n2) # helloworld

# Repetition / Broadcast Operation => Broadcast in string is doe usin + operator
message = "Hello"
print(message * 3) # HelloHelloHello

#Membership operation
print("m" in "message") # True
print("e" not in "message") # False

# Built-in functions
# 1. len() => It gives the levgth (total number of elements) of sequential datatypes i.e. list, string, tuple etc.

message= "Hello World"
print(len(message)) # 11

# 2. type() => return the type of any obhect
print(type(message)) # <class "str">

#slice() => this function is similar to string and list slicing

sliced_data = slice(2,7)
print(message[sliced_data]) # llo W

