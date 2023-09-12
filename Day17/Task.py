# create a class department with parameters  name and number_of_students
# create a method total students, which takes object as a parameter and return the total number of students from all
# departments.

class department:
    def __init__(self, no_of_students):
        self.no_of_students = no_of_students

    def total_students(self, other):
        return self.no_of_students + other.no_of_students

    def __add__(self,other):
        return self.no_of_students + other.no_of_students

d1 = department(10)
d2 = department(23)
result = d1.total_students(d2)
print(result) # 33

result = d1 + d2
print(result) # 33

# create a class Circle with an attribute radius. Create two objects of circle c1 and c2. Add the radius of the
# circles and print the result
# compare the size of the circle and

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def total_radius(self, other):
        return self.radius + other.radius

    def __gt__(self, other):
        return self.radius > other.radius


c1 = Circle(4)
c2 = Circle(5)

print(c1.radius + c2.radius)
result = c1.total_radius(c2)
print(result) # 9
print(c1>c2) # false

#using magic method
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __add__(self, other):
        return self.radius + other.radius
c1 = Circle(4)
c2 = Circle(5)
result = c1 + c2
print(result)