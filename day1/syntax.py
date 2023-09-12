### identifire###
# any name of a variable , function or class provided by the user is an identifier


# rules of naming identifiers
# 1. Identifiers are case sensitive i.e. area and Area are two different variables
# 2. identifiers can't be python keywords.
# 3. identifiers name can have A-Z, a-z, 0-9 and _
# 4. but it can't start with digit, 2a= "hello", here 2a is invalid identifier.
# 5. we can't use special symbols @,%,

### python statement###
# each line in a python code is an statement
#we can seperate multiple statements in same line using semicolon';'
# we can also use back slash \, for the line continuation

message = "hello world"
message1 = "hello" ; message2 = "world"
message = "hello" \
          "world"

### Indentation in python is very important to represent a code-block
# Let's see an if code block in C language

# if(a==1){
# printf("hello world")
#
#}

a=3
if a==2:
    print("hello world")
    if b==3:
        print("2 is also printed")
    print("this is outside b")
print("this is not in if code block")