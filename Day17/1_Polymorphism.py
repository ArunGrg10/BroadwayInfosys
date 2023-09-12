# Polymorphism in python refers to many form s of the same functions or objects
# sum(), len(), max(), min() etc. they are some of the examples which follows polymorphism.
# These built-in functions can take different datatype





# Function / Method overrloading

def addition(a,b):
    return a+b
def addition(a,b,c):
    return a+b+c

result = addition(1, 2) # it raiese Type Error.
print(result)
result = addition(1,2,3)
print(result)

# though addition() is defined twice, only the latest definition is considered. So, Python
# doesnot support function overloading

# But we can give default argument so tghat we can pass both two and three arguments in the function call
def addition(a, b, c=0):
    return a + b+c

result = addition(1,2)
print(result) #3
result= addition(1,2,3)
print(result) #6

class Employee:
    salary = 1200

    def descriptiion(self):
        retrun self.salary

    def description(self):
        return f"Salary is {self.salary}"

e = Employee()
print(e.employee()) # the last defination is considered. SO the result is "Salary is 1200"
