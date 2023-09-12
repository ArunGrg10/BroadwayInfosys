# conditions are used for makin decisions in a program
# There are four varieties of conditions we ccan create
# Simple if
# 2. if...else condition
# 3. if....elif...else ladder
# 4. nested if

# In the if conditons, the statement after the "if" is checked. If the statement is truthy then
# the condition is satisfied and the block inside the "if" is executed. Otherwise, it is not executed

a= 20
if a > 15:
    print(" the number is greater than 15")

if a:
    print(f"the number is {a}")

# if...else
if a> 15:
    print(" the number is greatwe than 15")
else:
    print("the number is smaller than 15")

if a:
    print(f"the number is {a}")
else:
    print("the number is 0")

# if...elif...else ladder

exam_mark = 76
if exam_mark >= 80:
    print("scored distinction")
elif exam_mark >= 65:
    print("scored first division")
elif exam_mark >= 55:
    print("scored second division")
elif exam_mark >= 40:
    print("scored third dicision")
else:
    print("failed")

# nestee if
a = 20
if a > 10:
    if a>15:
        print(f"{a}is greater than 15")
    else:
        print(f"{a} is just greater than a")
else:
    print(f"{a} is less than 10 ")


# ternary if
# One-linear conditions are called ternary if
a = 10
b = 5

if a > b:
    print("a is greater")
else:
    print("b is greater")
print("a is greater") if a > b else print("b is greater") # One-linear ternary if