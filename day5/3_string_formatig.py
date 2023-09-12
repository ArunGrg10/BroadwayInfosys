# We do sting formatting using f-string

programming_language = input("Enter a language")
message = f"I am learning {programming_language}"
print(message)

name= "arun"
age= 26
message = f" I am {name} and i am {age} years old."
print(message)

print('I am %s and i am %d years old' %(name, age))
print('I am {}'.format(name))
print('I am {} years old'.format(age))