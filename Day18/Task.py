# take two numbers as input and add those numbers. Handle the
# possible exceptions

try:
    a = int(input("enter a number1: "))
    b = int(input("enter numbeer2: "))
except Exception as e:
    print(e)
    print("please enter valid number")
else:
    add = a+b
    print(add)
finally:
    print(f"the addition result is {add}")


# task 2
# create a dictionary student with keys id, name, age, department. Take
# a input from the user, which info (id, name, age or department) he wants
# to access and pint the result. Handle the possible exceptions.

student = {"name": "arun","age": 21, "department": "bex", "id":34}
try:
    key = input("enter the key you want ot access ")
    data = student[key]

except KeyError:
    print("please enter a key present in the dictionary")
else:
    print(f"the {key} of the student is {data}")

# create a function to check whether an input character is vowel or not.
# Handle the possible exception.

 def is_vowel(char):
     if type(char) != str:
         return False
     if any([char.isnumeric(), len(char)>1, type(char) != str]):
         return False

     return char.lower() in ["a","e", "i", "o","u"]

character = input("enter a char: ")
result = is_vowel(character)
print(result)


#
