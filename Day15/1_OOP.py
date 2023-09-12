# OOp is an approach of programming in which programs are modeled in the real world-problems
# OOP isstands for Object Oriented Programming
# It has two major aspects; Class and Objects
# Class is the blouprint of an object. It has its own attributes known as properties and methods
#
# There are four major pillars of OOP
# 1. Inheritance
# 2. Encapsulation
# 3. Polymorphism
# 4. Abstraction

class Vehicle:
    engine_type = "Petrol" # class attribute

    def __init__(self, number_of_doors, color):
        self.number_of_doors = number_of_doors # instance attribute
        self.color = color # instance attribute

vehicle = Vehicle(4, "red")
print(vehicle.engine_type) # petrol
print(vehicle.number_of_doors) # 4
print(vehicle.color) # red
print(Vehicle.engine_type) # Petrol

print(Vehicle.color) # attribute error because color is an instance attribute but Vehicle is a class attribute

# In this Vehicle class "engine_type" is






# In this Vehicle alss "engine_type" is a class attribute, color and number of doors are instance
# attrinutes and __init__() is a constructor






#  Class have properties and methods which are collectively termed as "attributes"

# Let's set attribute in the objects
v2 = Vehicle("2", "green")
print(v2.color) # green; getting balue from the onject
v2.color = "red" # setting the value in object
print(v2.color) # red

print(v2.description())
