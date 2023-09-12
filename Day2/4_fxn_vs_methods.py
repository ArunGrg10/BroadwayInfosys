def addition(a, b):
    return a+b
print(addition(3,4))
# here addition is a user-defined function
# there several built-in functions len(), print(), map(), reduce(), filter(), sum()


class student:
        def age_after_ten_years(self, current_age):
            return current_age + 10

student1 = student()
age_after_ten_years = student1.age_after_ten_years(10)
print(age_after_ten_years)

 # here age after ten years is a method of class student which can be called using student object only


