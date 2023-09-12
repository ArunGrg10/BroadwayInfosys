# Classmethods are teh mehtods which takes calss as teh first parameter rather than self
# class method is created using @classmethod
# Static methods are teh methods which neither takes class nor self as a parmeter. They are like
# a normal function which doesn't change the state of the class
# Static method is created using @staticmethod decorator

class Student:
    def __init__(self, age):
        self.age = age

    @classmethod
    def from_birth_year(cls,year):
        age = 2023 - year
        return cls(age)

    @staticmethod
    def institution_name():
        return "Broadway"

s1 = Student(23)
print(s1.age) # 23
s2 = Student.from_birth_year(1992)
print(s2.age)


print(s2.institution_name())

# here "from_birth_year" method is a class mehtod. And it is also sometimes termed as a " factory method"

