#Author:Rinat.R
#Date:11.08.25
#Problem 6:
"""this program display the model, year, color,type and manufacturer of the car"""
class car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_color(self):
        return self.color
    def get_type(self):
        return self.type
    def get_manufacturer(self):
        return self.manufacturer
    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + self.type + ' ' + self.manufacturer
car1 = car("Supra", 2012, "Red", "Hatchback", "Toyota")
car2 = car("XTS", 2020, "Yellow", "Limousine", "Cadillac")
car1.fullspecs()
car2.fullspecs()

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())