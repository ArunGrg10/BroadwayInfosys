# Encapsulation is the process of hiding data in OOP approach proagramming
# We can make the attributes private, public and protected
# In pythons, protected members can be created using a single  underscore(_)  and private  members cab
# be created using  double underscore (__)

class vehicle:
    _color = "blue" # This is a protected property

    def __init__(self, doors, speed):
        self._doors = doors
        self._speed = speed

    def description(self):
        return f"color is {self._color}. Doors are {self._door} and speed is {self._speed}"

    def set_color(self, color):
        self._color = color

    def get_color():
        return self._color

v1 =  vehicle(4,120)
print(v1._color) # Accessing protected member outside the class is not recommended

v1.set_color("green")
print(v1.get_color())

# Protected member of class are meant to be used within a class or within their children class only.
# They are not menat to be used outside the class
# Python is not strict in OOP approach. So, it allows protected member to be accessed even outside the class
# But, this is not recommended to for developers as this does not follow proper convention.

# Private property is not accesible outside the class or in the children classes.
print(v1.__mileage) # it raises attribute error becz __mileage is private property

print(dir(v1))

private(v1._vehicle__mileage) #50

# Though __mileage is a privagte property, we can access this property by _vehicle__mileage. This is also called
# as "name mangling" in Python.

