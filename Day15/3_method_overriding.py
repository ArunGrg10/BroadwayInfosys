class Vehicle:
    def __init__(self, color, doors):
        self.color = color
        self.doors = doors

    def get_details(self):
        return f"color is {self.color} and doors are {self.doors}"

class Bike(Vehicle):
    def __init__(self, color, doors, mileage, company):
        super().__init__(color,doors)
        self.mileage = mileage
        self.company = company

    def get_details(self):
        print(super().get_details())
        return f"mileage is {self.mileage} and company is {self.company}"

b = Bike("red", 0,45, "yamaha")
print(b.get_details())
